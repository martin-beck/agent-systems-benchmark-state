#!/usr/bin/env bash
set -euo pipefail

readonly TLA_VERSION=1.7.4
readonly TLA_SHA256=936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88
readonly SPEC_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly TEMP_DIR="$(mktemp -d)"
trap 'rm -rf -- "${TEMP_DIR}"' EXIT

readonly JAR="${TEMP_DIR}/tla2tools.jar"
readonly URL="https://github.com/tlaplus/tlaplus/releases/download/v${TLA_VERSION}/tla2tools.jar"

curl --fail --location --retry 3 --show-error --silent --output "${JAR}" "${URL}"
printf '%s  %s\n' "${TLA_SHA256}" "${JAR}" | sha256sum --check --strict

run_model() {
    local model="$1"
    java -XX:+UseParallelGC -cp "${JAR}" tlc2.TLC -cleanup \
        -config "${SPEC_DIR}/${model}.cfg" -metadir "${TEMP_DIR}/${model}-states" \
        -workers auto "${SPEC_DIR}/${model}.tla"
}

run_model HandoffctlBinding
run_model HandoffctlLocks
run_model Handoffctl
