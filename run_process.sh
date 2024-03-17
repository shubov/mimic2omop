#!/bin/bash

# Stop execution if any command fails
set -e

# Google Cloud SDK
# curl https://sdk.cloud.google.com | bash
export PATH="$PATH:~/google-cloud-sdk/bin"
gcloud auth login

# MIMIC to OMOP Conversion
cd src/MIMIC/
cd vocabulary_refresh
# python3 vocabulary_refresh.py -s10 && \
python3 vocabulary_refresh.py -s20 && \
python3 vocabulary_refresh.py -s30
cd ../
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_ddl.conf && \
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_staging.conf && \
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_etl.conf && \
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_ut.conf && \
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_metrics.conf && \
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_unload.conf

# More commands can be added here following the same pattern.

# Remember to navigate back to the root directory or any specific directory as needed.

