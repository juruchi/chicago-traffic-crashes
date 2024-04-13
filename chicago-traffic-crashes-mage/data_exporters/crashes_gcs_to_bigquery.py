if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(*args, **kwargs):
# if 'custom' not in globals():
#     from mage_ai.data_preparation.decorators import custom
# if 'test' not in globals():
#     from mage_ai.data_preparation.decorators import test


# @custom
# def transform_custom(*args, **kwargs):
    from google.cloud import bigquery
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/keys/my-creds.json"
    client = bigquery.Client()

    project_id = os.environ.get('TF_VAR_project_id')
    dataset_id = 'processed_data'
    gcs_folder = 'crashes'
    table_id = gcs_folder+'_external'


    job_config = bigquery.QueryJobConfig()
    # Set the destination table
    table_ref = client.dataset(dataset_id).table(table_id)
    # job_config.destination = table_ref
    sql = f"""
        CREATE OR REPLACE EXTERNAL TABLE `{project_id}.{dataset_id}.{table_id}`
        WITH PARTITION COLUMNS
        OPTIONS (
        uris = ['gs://{project_id}-traffic-crash-data/{gcs_folder}/*'],
        format = 'PARQUET',
        hive_partition_uri_prefix = 'gs://{project_id}-traffic-crash-data/{gcs_folder}'
        );

        CREATE OR REPLACE TABLE {project_id}.{dataset_id}.{gcs_folder}_partition
        PARTITION BY crash_date AS
        SELECT * FROM `{project_id}.{dataset_id}.{table_id}`;
    """

    # Start the query, passing in the extra configuration.
    query_job = client.query(
        sql,
        # Location must match that of the dataset(s) referenced in the query
        # and of the destination table.
        location="us-central1",
        job_config=job_config,
    )  # API request - starts the query

    query_job.result()  # Waits for the query to finish
    print("Query results loaded to table {}".format(table_ref.path))