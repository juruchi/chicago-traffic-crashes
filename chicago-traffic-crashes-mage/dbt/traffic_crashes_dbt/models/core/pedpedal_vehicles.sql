{# Extract vehicles (and crash_record_id) for crashes involving a vehicle and a pedestrian and/or bicycle #}
{{ config(materialized='table') }}

select crash_unit_id, crash_record_id, crash_date, unit_type, exceed_speed_limit_i
from {{ ref("stg_vehicles") }}
where crash_record_id in (
    select distinct crash_record_id
    FROM {{ ref("stg_vehicles") }}
    group by crash_record_id
    having count(distinct unit_type) > 1 and count(case when unit_type='DRIVER' then 1 end) >= 1
) and crash_record_id in (
    select distinct crash_record_id
    from {{ ref("stg_vehicles") }}
    group by crash_record_id
    having count(distinct unit_type) > 1 and count(case when unit_type in ('PEDESTRIAN', 'BICYCLE') then 1 end) >= 1
)
