{{ config(materialized='table') }}

{# select crash_record_id, crash_date, REPLACE(REPLACE(REPLACE(REPLACE(`location`, 'POINT ', ''), "(", ""), ")", ""), " ", ",") as `location`
from {{ ref("stg_crashes") }}
where crash_record_id in (
    select distinct crash_record_id
    FROM {{ ref("pedpedal_vehicles") }}
)  #}

select crash_record_id, crash_date, concat(latitude, ",", longitude) as lat_long
from {{ ref("stg_crashes") }}
where crash_record_id in (
    select distinct crash_record_id
    FROM {{ ref("pedpedal_vehicles") }}
) 