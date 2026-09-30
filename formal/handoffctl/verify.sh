#!/usr/bin/env bash
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
set -euo pipefail

if [[ "${1:-}" != "--tier" || ( "${2:-}" != "portable-smoke" && "${2:-}" != "pr-fast" && "${2:-}" != "pr-publication" && "${2:-}" != "full-exhaustive" ) || "$#" -ne 2 ]]; then
    echo "usage: $0 --tier portable-smoke|pr-fast|pr-publication|full-exhaustive" >&2
    exit 64
fi
readonly TIER="$2"
readonly ATTESTATION="${TLC_ATTESTATION_PATH:-${TMPDIR:-/tmp}/handoffctl-${TIER}-attestation.json}"

readonly TLA_VERSION=1.7.4
readonly TLA_SHA256=936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88
readonly SPEC_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly TEMP_DIR="$(mktemp -d)"
readonly MANIFEST="${TEMP_DIR}/outcomes.manifest"
: > "${MANIFEST}"
trap 'rm -rf -- "${TEMP_DIR}"' EXIT

readonly JAR="${TEMP_DIR}/tla2tools.jar"
readonly URL="https://github.com/tlaplus/tlaplus/releases/download/v${TLA_VERSION}/tla2tools.jar"

curl --fail --location --retry 3 --show-error --silent --output "${JAR}" "${URL}"
printf '%s  %s\n' "${TLA_SHA256}" "${JAR}" | sha256sum --check --strict

run_model() {
    local model="$1"
    local source="${2:-${model}}"
    local config="${SPEC_DIR}/${model}.cfg"
    # The fast tier has its own reduced configuration over the binding spec.
    if [[ "${model}" == "HandoffctlFast" ]]; then
        source=HandoffctlBinding
    elif [[ "${model}" == "OracleInteractionGates" ]]; then
        source=../oracle/OracleInteractionGates
        config="${SPEC_DIR}/../oracle/OracleInteractionGates.cfg"
    fi
    python3 "${SPEC_DIR}/../../tools/tlc_runner.py" \
        --jar "${JAR}" \
        --model "${SPEC_DIR}/${source}.tla" \
        --config "${config}" \
        --metadir "${TEMP_DIR}/${model}-states"
    printf "%s success\n" "${model}" >> "${MANIFEST}"
}

if [[ "${TIER}" == "portable-smoke" ]]; then
    # Smoke is deliberately non-exhaustive and never produces full evidence.
    run_model HandoffctlBinding
elif [[ "${TIER}" == "pr-fast" ]]; then
    # Deliberately smaller safety-only required merge gate.
    run_model HandoffctlFast
    run_model OracleInteractionGates
elif [[ "${TIER}" == "pr-publication" ]]; then
    # PR publication checks every invariant family. The general lifecycle
    # model uses a one-process configuration; weekly full evidence retains its
    # complete two-process cross-product.
    run_model HandoffctlBinding
    run_model HandoffctlLocks
    run_model HandoffctlRun
    run_model HandoffctlStorage
    run_model HandoffctlPR Handoffctl
    run_model HandoffctlRecovery
else
    run_model HandoffctlBinding
    run_model HandoffctlLocks
    run_model HandoffctlRun
    run_model HandoffctlStorage
    run_model Handoffctl
    run_model HandoffctlRecovery
fi
python3 "${SPEC_DIR}/attest.py" --tier "${TIER}" --output "${ATTESTATION}" --jar "${JAR}" --manifest "${MANIFEST}" \
    --models $(if [[ "${TIER}" == "portable-smoke" ]]; then echo HandoffctlBinding; elif [[ "${TIER}" == "pr-fast" ]]; then echo HandoffctlFast OracleInteractionGates; elif [[ "${TIER}" == "pr-publication" ]]; then echo HandoffctlBinding HandoffctlLocks HandoffctlRun HandoffctlStorage HandoffctlPR HandoffctlRecovery; else echo HandoffctlBinding HandoffctlLocks HandoffctlRun HandoffctlStorage Handoffctl HandoffctlRecovery; fi)
