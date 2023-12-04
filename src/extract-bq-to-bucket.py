import subprocess
import os

dataset_id = "booming-edge-403620:mimiciv_full_current_cdm"
bucket_name = "gs://shubov_mimic-iv"
tables = [
    "attribute_definition",
    "care_site",
    "cdm_source",
    "cohort",
    "cohort_attribute",
    "cohort_definition",
    "concept",
    "concept_ancestor",
    "concept_class",
    "concept_relationship",
    "concept_synonym",
    "condition_era",
    "condition_occurrence",
    "cost",
    "d_items_to_concept",
    "d_labitems_to_concept",
    "d_micro_to_concept",
    "death",
    "device_exposure",
    "domain",
    "dose_era",
    "drug_era",
    "drug_exposure",
    "drug_strength",
    "fact_relationship",
    "location",
    "measurement",
    "metadata",
    "note",
    "note_nlp",
    "observation",
    "observation_period",
    "payer_plan_period",
    "person",
    "procedure_occurrence",
    "provider",
    "relationship",
    "source_to_concept_map",
    "specimen",
    "visit_detail",
    "visit_occurrence",
    "vocabulary",
]

for table in tables:
    export_cmd = (
        f"bq extract --destination_format=PARQUET "
        f"'{dataset_id}.{table}' "
        f"'{bucket_name}/{table}/*.parquet'"
    )
    os.system(export_cmd)
