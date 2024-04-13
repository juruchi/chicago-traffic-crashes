import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    url = 'https://data.cityofchicago.org/resource/85ca-t3if.csv?$limit=2000000'
    response = requests.get(url)

    crash_dtypes = {
        'crash_record_id':str,
        'crash_date_est_i':str,
        'posted_speed_limit':pd.Int64Dtype(),
        'traffic_control_device':str,
        'device_condition':str,
        'weather_condition':str,
        'lighting_condition':str,
        'first_crash_type':str,
        'trafficway_type':str,
        'lane_cnt':pd.Int64Dtype(),
        'alignment':str,
        'roadway_surface_cond':str,
        'road_defect':str,
        'report_type':str,
        'crash_type':str,
        'intersection_related_i':str,
        'private_property_i':str,
        'hit_and_run_i':str,
        'damage':str,
        'prim_contributory_cause':str,
        'sec_contributory_cause':str,
        'street_no':pd.Int64Dtype(),
        'street_direction':str,
        'street_name':str,
        'beat_of_occurence':pd.Int64Dtype(),
        'photos_taken_i':str,
        'statements_taken_i':str,
        'dooring_i':str,
        'work_zone_i':str,
        'work_zone_type':str,
        'workers_present_i':str,
        'num_units':pd.Int64Dtype(),
        'most_severe_injury':str,
        'injuries_total':pd.Int64Dtype(),
        'injuries_fata':pd.Int64Dtype(),
        'injuries_incapacitating':pd.Int64Dtype(),
        'injuries_non_incapacitating':pd.Int64Dtype(),
        'injuries_reported_not_evident':pd.Int64Dtype(),
        'injuries_no_indication':pd.Int64Dtype(),
        'injuries_unkown':pd.Int64Dtype(),
        'crash_hour':pd.Int64Dtype(),
        'crash_day_of_week':pd.Int64Dtype(),
        'crash_month':pd.Int64Dtype(),
        'latitude':float,
        'longitude':float,
        'location':str
    }

    date_vars=["crash_date", "date_police_notified"]
    
    df = pd.read_csv(io.StringIO(response.text), sep=',', dtype=crash_dtypes, parse_dates=date_vars)

    df['crash_date'] = pd.to_datetime(df["crash_date"], format="%Y-%m-%dT%H:%M:%S.%f")
    df['date_police_notified'] = pd.to_datetime(df["date_police_notified"], format="%Y-%m-%dT%H:%M:%S.%f")

    return df


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'

@test
def test_output(output, *args) -> None:
    
    assert output["crash_record_id"].is_unique is True, 'The dataset unique identifier contains duplicates'

