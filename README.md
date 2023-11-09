# Project template: GPU
This repository represents a blueprint for Python projects using pyTorch optimized with NVIDIA GPUs. The image pre-install the following software components:

- Python 3.8
- Anaconda with a default environment
    - pyTorch
    - Linter for appropiate code standards (and config files for reasonable defaults)
        - flake8
        - pyLint
    - Code formatter: black
- NVIDIA toolchain
    - CUDA
    - cuBLAS
    - NVIDIA cuDNN
    - NVIDIA NCCL (optimized for NVLink)
    - RAPIDS
    - NVIDIA Data Loading Library (DALI)
    - TensorRT
    - Torch-TensorRT

## Usage
Specify the packages you require in the *requirements.txt*. More complex environment customization goes into *Dockerfile*.

While using Visual Studio Code for development is encouraged, the image does not depend on this IDE in any way. As a side effect, its required server components are not even installed by default if the Dockerfile in root is built manually. Opening the project in VS Code will set the proper default and configure everything appropriately. Alternatively, build the container with `docker build -t <YOUR PROJECT NAME>:0.1 .` and run the container with `docker run -p <YOUR LOCAL PORT>:22 --rm --gpus all <YOUR PROJECT NAME>:0.1`.

# Notes

## Google Cloud SDK
```bash
curl https://sdk.cloud.google.com | bash
export PATH="$PATH:~/google-cloud-sdk/bin"
gcloud auth login
```

## mimic2omop flow
```bash
cd src/MIMIC/
cd vocabulary_refresh
python3 vocabulary_refresh.py -s10
python3 vocabulary_refresh.py -s20
python3 vocabulary_refresh.py -s30
cd ../
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_ddl.conf
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_staging.conf
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_etl.conf
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_ut.conf
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_metrics.conf
python3 scripts/run_workflow.py -e conf/full.etlconf -c conf/workflow_unload.conf
```
## load MIMIC from Nexcloud volume to Google Cloud Bucket
create script file
```bash
nano load_csv_files.sh
```
paste this code in the script file
```bash
#!/bin/bash

# Set your Google Cloud project and dataset
PROJECT_ID="your-project-id"
DATASET="mimiciv_hosp"

# Loop through all CSV files in the current directory
for file in *.csv.gz; do
  # Extract the table name from the filename (assuming filenames are table names)
  table_name=$(basename "$file" .csv.gz)

  # Create the table in BigQuery and upload the data
  bq load --autodetect --source_format=CSV "${PROJECT_ID}:${DATASET}.${table_name}" "$file"
done
```
give the correct permissions to the script 
```bash
chmod +x load_csv_files.sh
```
then run the script
## tmux install
```bash
sudo apt-get update
sudo apt-get install tmux
```
## Download Waveforms data and upload to Google Cloud Bucket
https://physionet.org/content/mimic4wdb/0.1.0/waves/#files-panel

```bash
wget -r -N -c -np https://physionet.org/files/mimic4wdb/0.1.0/ > wget.log 2>&1 &
gsutil cp physionet.org/* gs://shubov-athena/waveforms
```