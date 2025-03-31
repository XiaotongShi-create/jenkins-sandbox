from google.cloud import storage, bigquery

# Initialize clients
storage_client = storage.Client()
bq_client = bigquery.Client()

# GCS bucket and file
bucket_name = "jenkins-pipeline"
csv_filename = "Electric_Vehicle_Population_Data.csv"

# Upload CSV to GCS
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(csv_filename)
blob.upload_from_filename(csv_filename)
print("CSV uploaded to GCS.")

# Load CSV into BigQuery
dataset_id = "jenkins_sandbox"
table_id = "Electric_Vehicle_Population"

job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, autodetect=True)
uri = f"gs://{bucket_name}/{csv_filename}"
load_job = bq_client.load_table_from_uri(uri, f"{dataset_id}.{table_id}", job_config=job_config)
load_job.result()
print("Data loaded into BigQuery.")
