#!/bin/bash
set -euo pipefail

ml conda
conda activate pyfmri

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

python "${SCRIPT_DIR}/region_ISC.py" "$SLURM_ARRAY_TASK_ID" --verbose