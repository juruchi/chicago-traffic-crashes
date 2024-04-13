import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    url = 'https://data.cityofchicago.org/resource/u6pd-qa9d.csv?$limit=2000000'
    response = requests.get(url)

    people_dtypes = {
        'person_id':str,
        'person_type':str,
        'crash_record_id':str,
        'vehicle_id':str,
        'seat_no':str,
        'city':str,
        'state':str,
        'zipcode':str,
        'sex':str,
        'age':pd.Int64Dtype(),
        'drivers_license_state':str,
        'drivers_licese_class':str,
        'safety_equipment':str,
        'airbag_deployed':str,
        'ejection':str,
        'injury_classification':str,
        'hospital':str,
        'ems_agency':str,
        'ems_run_no':str,
        'driver_action':str,
        'driver_vision':str,
        'physical_condition':str,
        'pedpedal_action':str,
        'pedpedal_visibility':str,
        'pedpedal_location':str,
        'bac_result':str,
        'bac_result_value':float,
        'cell_phone_use':str
    }

    date_vars=["crash_date"]
    
    df = pd.read_csv(io.StringIO(response.text), sep=',', dtype=people_dtypes, parse_dates=date_vars)

    df['crash_date'] = pd.to_datetime(df["crash_date"], format="%Y-%m-%dT%H:%M:%S.%f")

    return df


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'

@test
def test_output(output, *args) -> None:
    
    assert output["person_id"].is_unique is True, 'The dataset unique identifier contains duplicates'

