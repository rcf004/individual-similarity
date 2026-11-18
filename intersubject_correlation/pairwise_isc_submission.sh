#!/bin/bash
set -euo pipefail


REGION_FILE=/N/project/NimbleMRI/SNACK_Kretzel/code/level2/eTS/custom_parc/schaefer200_tian1_labels.txt
REGION_COUNT=$(awk 'NF && $1 !~ /^#/ {n++} END {print n+0}' "$REGION_FILE")
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LOGDIR="${SCRIPT_DIR}/logs/$(date +'%Y%m%d-%H%M%S')"

accountID=${ACC_ID} 		        # required for IU slurm submission
email=${EMAIL}       	            # for SLURM email notifications
curTime=`date +"%Y%m%d-%H%M%S"`     # pull date for -o/-e logs

mkdir -p "$LOGDIR"                  # make log directory


echo "YOUR ARRAY WILL ASSUME $REGION_COUNT REGIONS. CHECK THIS COUNT IS CORRECT."
echo "Submitting region indices 0-$((REGION_COUNT - 1))."

sbatch \
    -A ${accountID} \
    --mail-user=${email} \
    --mail-type=END,FAIL,ARRAY_TASKS \
    --array="0-$((REGION_COUNT - 1))%10" \
    --nodes=1 \
    --mem=16G \
    -o "${LOGDIR}/OUTPUT_region_%A_%a.txt" \
    -e "${LOGDIR}/ERROR_region_%A_%a.txt" \
    --job-name=region-isc \
    --time=2:00:00 \
    "${SCRIPT_DIR}/region-isc.sbatch"

