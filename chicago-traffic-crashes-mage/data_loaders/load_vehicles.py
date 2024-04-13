import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    url = 'https://data.cityofchicago.org/resource/68nd-jvt3.csv?$limit=2000000'
    response = requests.get(url)

    vehicle_dtypes = {
        'crash_unit_id':pd.Int64Dtype(),
        'crash_record_id':str,
        'unit_no':pd.Int64Dtype(),
        'unit_type':str,
        'num_passengers':pd.Int64Dtype(),
        'vehicle_id':pd.Int64Dtype(),
        'cmrc_veh_i':str,
        'make':str,
        'model':str,
        'lic_plate_state':str,
        'vehicle_year':pd.Int64Dtype(),
        'vehicle_defect':str,
        'vehicle_type':str,
        'vehicle_use':str,
        'travel_direction':str,
        'maneuver':str,
        'towed_i':str,
        'fire_i':str,
        'occupant_cnt':pd.Int64Dtype(),
        'exceed_spped_limit_i':str,
        'towed_by':str,
        'towed_to':str,
        'area_00_i':str,
        'area_01_i':str,
        'area_02_i':str,
        'area_03_i':str,
        'area_04_i':str,
        'area_05_i':str,
        'area_06_i':str,
        'area_07_i':str,
        'area_08_i':str,
        'area_09_i':str,
        'area_10_i':str,
        'area_11_i':str,
        'area_12_i':str,
        'area_99_i':str,
        'first_contact_point':str,
        'cmv_id':pd.Int64Dtype(),
        'usdot_no':str,
        'ccmc_no':str,
        'ilcc_no':str,
        'commercial_src':str,
        'gvwr':str,
        'carrier_name':str,
        'carrier_state':str,
        'carrier_city':str,
        'hazmat_placards_i':str,
        'hazmat_name':str,
        'un_no':str,
        'hazmat_present_i':str,
        'hazmat_report_i':str,
        'hazmat_report_no':str,
        'hazmat_vio_cause_crash_i':str,
        'mcs_vio_cause_crash_i':str,
        'idot_permit_no':str,
        'wide_load_i':str,
        'trailer1_width':str,
        'trailer2_width':str,
        'trailer1_length':pd.Int64Dtype(),
        'trailer2_length':pd.Int64Dtype(),
        'total_vehicle_length':pd.Int64Dtype(),
        'axle_cnt':pd.Int64Dtype(),
        'vehicle_config':str,
        'cargo_body_type':str,
        'load_type':str,
        'hazmat_out_of_service_i':str,
        'mcs_out_of_service_i':str,
        'hazmat_class':str
    }

    date_vars=["crash_date"]
    
    # return pd.read_csv(io.StringIO(response.text), sep=',', dtype=vehicle_dtypes, parse_dates=date_vars, date_format="%Y-%m-%dT%H:%M:%S.%f")
    df = pd.read_csv(io.StringIO(response.text), sep=',', dtype=vehicle_dtypes, parse_dates=date_vars)

    df['crash_date'] = pd.to_datetime(df["crash_date"], format="%Y-%m-%dT%H:%M:%S.%f")
    
    return df


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'

@test
def test_output(output, *args) -> None:
    
    assert output["crash_unit_id"].is_unique is True, 'The dataset unique identifier contains duplicates'
