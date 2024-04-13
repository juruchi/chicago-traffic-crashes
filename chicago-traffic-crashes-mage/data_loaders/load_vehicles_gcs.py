import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.dataset as ds
import os


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/keys/my-creds.json"

project_id = os.environ.get('TF_VAR_project_id')
bucket_name = project_id + "-traffic-crash-data"
table_name = "vehicles"

root_path = f'{bucket_name}/{table_name}'

@data_loader
def load_data(*args, **kwargs):

    gcs = pa.fs.GcsFileSystem()

    dataset = ds.dataset(
        source=root_path,
        format="parquet",
        filesystem=gcs
    )

    pyarrow_table = dataset.to_table()
    df = pyarrow_table.to_pandas()
    return df


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'
