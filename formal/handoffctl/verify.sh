#!/usr/bin/env bash
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
set -euo pipefail

if [[ "${1:-}" != "--tier" || ( "${2:-}" != "portable-smoke" && "${2:-}" != "pr-fast" && "${2:-}" != "pr-publication" && "${2:-}" != "full-exhaustive" ) ]]; then
    echo "usage: $0 --tier portable-smoke|pr-fast|pr-publication|full-exhaustive [--diagnostic-queue ABSOLUTE_PATH --diagnostic-admission-lock ABSOLUTE_PATH]" >&2
    exit 64
fi
readonly TIER="$2"
shift 2
if [[ -n "${TLC_DIAGNOSTICS_DIR:-}" && "${TIER}" != "full-exhaustive" ]]; then
    echo "TLC_DIAGNOSTICS_DIR is reserved for exploratory full-exhaustive runs" >&2
    exit 64
fi
EXECUTION_CLASSIFICATION=canonical
RUNNER_ADMISSION_ARGS=()
if [[ "$#" -eq 4 && "$1" == "--diagnostic-queue" && "$3" == "--diagnostic-admission-lock" ]]; then
    if [[ "$2" != /* || "$4" != /* || "$2" == "$4" ]]; then
        echo "diagnostic admission paths must be distinct absolute paths" >&2
        exit 64
    fi
    EXECUTION_CLASSIFICATION=diagnostic-private-admission
    RUNNER_ADMISSION_ARGS=(--queue "$2" --admission-lock "$4")
elif [[ "$#" -ne 0 ]]; then
    echo "diagnostic queue and admission lock must be supplied together after --tier" >&2
    exit 64
fi
readonly EXECUTION_CLASSIFICATION
readonly ATTESTATION="${TLC_ATTESTATION_PATH:-${TMPDIR:-/tmp}/handoffctl-${TIER}-attestation.json}"

# These are end-to-end verifier budgets, rather than per-model TLC deadlines:
# fetching the pinned verifier, queue admission, every model, and attestation
# all consume the same allowance.  The checked-in tier policy fixes each value.
case "${TIER}" in
    portable-smoke) readonly TIER_BUDGET_SECONDS=600 ;;
    pr-fast) readonly TIER_BUDGET_SECONDS=300 ;;
    pr-publication) readonly TIER_BUDGET_SECONDS=900 ;;
    full-exhaustive) readonly TIER_BUDGET_SECONDS=86400 ;;
esac
readonly DECLARED_BUDGET_SECONDS="${TLC_BUDGET_SECONDS:-${TIER_BUDGET_SECONDS}}"
if [[ ! "${DECLARED_BUDGET_SECONDS}" =~ ^[1-9][0-9]*$ ]] || (( DECLARED_BUDGET_SECONDS != TIER_BUDGET_SECONDS )); then
    echo "${TIER} requires an aggregate verifier budget of ${TIER_BUDGET_SECONDS} seconds" >&2
    exit 64
fi
readonly START_EPOCH_SECONDS="$(date +%s)"

elapsed_seconds() {
    echo $(( $(date +%s) - START_EPOCH_SECONDS ))
}

remaining_seconds() {
    local remaining=$(( DECLARED_BUDGET_SECONDS - $(elapsed_seconds) ))
    if (( remaining < 1 )); then
        echo "${TIER} aggregate verifier budget exhausted (including admission)" >&2
        exit 124
    fi
    echo "${remaining}"
}

# The runner and receipt must describe the same effective resource contract.
# Workflows normally provide these values, but a direct local invocation must
# remain self-contained rather than completing TLC and failing at attestation.
export TLC_MEMORY_MAX="${TLC_MEMORY_MAX:-3G}"
export TLC_SWAP_MAX="${TLC_SWAP_MAX:-3G}"

readonly TLA_VERSION=1.7.4
readonly TLA_SHA256=936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88
readonly SPEC_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly WORK_ROOT="${TLC_WORK_ROOT:-${TMPDIR:-/tmp}/agent-workflow-coordinator-tlc}"
if [[ "${WORK_ROOT}" != /* ]]; then
    echo "TLC_WORK_ROOT must be an absolute path" >&2
    exit 64
fi
mkdir --mode=700 --parents "${WORK_ROOT}"
readonly TEMP_DIR="$(mktemp -d "${WORK_ROOT}/handoffctl-${TIER}.XXXXXX")"
readonly SLICE_DIR="${SPEC_DIR}/.tlc-slices-$$"
readonly MANIFEST="${TEMP_DIR}/outcomes.manifest"
: > "${MANIFEST}"
preserve_diagnostics() {
    local exit_status="$?"
    local diagnostic_dir="${TLC_DIAGNOSTICS_DIR:-}"
    if [[ -n "${diagnostic_dir}" ]]; then
        mkdir --mode=700 --parents "${diagnostic_dir}"
        cp -- "${MANIFEST}" "${diagnostic_dir}/outcomes.manifest" 2>/dev/null || true
        if [[ -n "${RUNNER_ADMISSION_ARGS[*]}" ]]; then
            cp -- "${RUNNER_ADMISSION_ARGS[1]}"/*.outcome.json "${diagnostic_dir}/" 2>/dev/null || true
        fi
        python3 - "${diagnostic_dir}/exploratory-receipt.json" "${TIER}" "${exit_status}" <<'PY'
import json
import sys

output, tier, status = sys.argv[1:]
with open(output, "w", encoding="utf-8") as handle:
    json.dump(
        {
            "schema_version": 1,
            "classification": "exploratory",
            "profile": tier,
            "complete": status == "0",
            "exit_status": int(status),
            "non_claim": "partial, interrupted, and failed stress runs are exploratory diagnostics only",
        },
        handle,
        indent=2,
        sort_keys=True,
    )
    handle.write("\n")
PY
    fi
    rm -rf -- "${TEMP_DIR}" "${SLICE_DIR}"
}
trap preserve_diagnostics EXIT

readonly JAR="${TEMP_DIR}/tla2tools.jar"
readonly URL="https://github.com/tlaplus/tlaplus/releases/download/v${TLA_VERSION}/tla2tools.jar"

timeout --foreground --signal=TERM --kill-after=5s "$(remaining_seconds)" \
    curl --fail --location --retry 3 --show-error --silent --output "${JAR}" "${URL}"
timeout --foreground --signal=TERM --kill-after=5s "$(remaining_seconds)" \
    bash -c 'printf "%s  %s\\n" "$1" "$2" | sha256sum --check --strict' \
    -- "${TLA_SHA256}" "${JAR}"

run_model() {
    local model="$1"
    local source="${2:-${model}}"
    local config="${3:-${SPEC_DIR}/${model}.cfg}"
    local model_path
    # The fast tier has its own reduced configuration over the binding spec.
    if [[ "${model}" == "HandoffctlFast" ]]; then
        source=HandoffctlBinding
    elif [[ "${model}" == "HandoffctlReceiptsFast" ]]; then
        source=HandoffctlReceipts
    elif [[ "${model}" == "HandoffctlPublicationFast" ]]; then
        source=HandoffctlPublication
        config="${SPEC_DIR}/HandoffctlPublicationFast.cfg"
    elif [[ "${model}" == "OracleInteractionGates" ]]; then
        source=../oracle/OracleInteractionGates
        config="${SPEC_DIR}/../oracle/OracleInteractionGates.cfg"
    fi
    if [[ "${source}" == /* ]]; then
        model_path="${source}.tla"
    else
        model_path="${SPEC_DIR}/${source}.tla"
    fi
    # timeout encloses queue/lock admission as well as TLC execution.  The
    # per-model runner deadline is capped to the remaining aggregate budget.
    local remaining
    remaining="$(remaining_seconds)"
    timeout --foreground --signal=TERM --kill-after=5s "${remaining}" \
        python3 "${SPEC_DIR}/../../tools/tlc_runner.py" \
        --jar "${JAR}" \
        --model "${model_path}" \
        --config "${config}" \
        --metadir "${TEMP_DIR}/${model}-states" \
        --workspace "${TEMP_DIR}" \
        --storage-max "${TLC_STORAGE_MAX:-2G}" \
        --storage-reserve "${TLC_STORAGE_RESERVE:-256M}" \
        --timeout-seconds "${remaining}" \
        "${RUNNER_ADMISSION_ARGS[@]}"
    printf "%s success\n" "${model}" >> "${MANIFEST}"
}

if [[ "${TIER}" == "portable-smoke" ]]; then
    # Smoke is deliberately non-exhaustive and never produces full evidence.
    run_model HandoffctlBinding
elif [[ "${TIER}" == "pr-fast" ]]; then
    # Deliberately smaller safety-only required merge gate.
    run_model HandoffctlFast
    run_model HandoffctlReceiptsFast HandoffctlReceipts
    run_model HandoffctlPublicationFast HandoffctlPublication
    run_model HandoffctlObservation
    run_model OracleInteractionGates
elif [[ "${TIER}" == "pr-publication" ]]; then
    # PR publication checks every invariant family. HandoffctlLiveness is the
    # documented one-process liveness abstraction; weekly full evidence retains
    # the complete two-process cross-product.
    run_model HandoffctlBinding
    run_model HandoffctlLocks
    run_model HandoffctlRun
    run_model HandoffctlStorage
    run_model HandoffctlReceipts
    run_model HandoffctlPublication
    run_model HandoffctlObservation
    run_model HandoffctlLiveness Handoffctl
    run_model HandoffctlRecovery
else
    run_model HandoffctlBinding
    run_model HandoffctlLocks
    run_model HandoffctlRun
    run_model HandoffctlStorage
    run_model HandoffctlReceipts
    run_model HandoffctlPublication
    run_model HandoffctlObservation
    # `operation` is immutable. These p1 operation slices partition the
    # original two-process aggregate model exactly; p2 retains its full domain.
    mapfile -t local_operations < <(
        cd "${SPEC_DIR}" && python3 -c 'from slices import OPERATIONS; print(*OPERATIONS, sep="\n")'
    )
    mkdir --mode=700 "${SLICE_DIR}"
    for operation_name in "${local_operations[@]}"; do
        slice_module="$(cd "${SPEC_DIR}" && python3 -c 'import sys; from slices import module_name; print(module_name(sys.argv[1]))' "${operation_name}")"
        slice="${SLICE_DIR}/${slice_module}"
        python3 "${SPEC_DIR}/slices.py" --base-source "${SPEC_DIR}/Handoffctl.tla" --operation "${operation_name}" --output-source "${slice}.tla"
        cp -- "${SPEC_DIR}/Handoffctl.cfg" "${slice}.cfg"
        run_model "HandoffctlSlice-${operation_name}" "${slice}" "${slice}.cfg"
    done
    run_model HandoffctlRecovery
fi
timeout --foreground --signal=TERM --kill-after=5s "$(remaining_seconds)" \
    python3 "${SPEC_DIR}/attest.py" --tier "${TIER}" --output "${ATTESTATION}" --jar "${JAR}" --manifest "${MANIFEST}" --execution-classification "${EXECUTION_CLASSIFICATION}" --budget-seconds "${DECLARED_BUDGET_SECONDS}" --started-epoch "${START_EPOCH_SECONDS}" \
    --models $(if [[ "${TIER}" == "portable-smoke" ]]; then echo HandoffctlBinding; elif [[ "${TIER}" == "pr-fast" ]]; then echo HandoffctlFast HandoffctlReceiptsFast HandoffctlPublicationFast HandoffctlObservation OracleInteractionGates; elif [[ "${TIER}" == "pr-publication" ]]; then echo HandoffctlBinding HandoffctlLocks HandoffctlRun HandoffctlStorage HandoffctlReceipts HandoffctlPublication HandoffctlObservation HandoffctlLiveness HandoffctlRecovery; else printf 'HandoffctlBinding HandoffctlLocks HandoffctlRun HandoffctlStorage HandoffctlReceipts HandoffctlPublication HandoffctlObservation '; (cd "${SPEC_DIR}" && python3 -c 'from slices import OPERATIONS; print(*(f"HandoffctlSlice-{operation}" for operation in OPERATIONS))'); echo HandoffctlRecovery; fi)
