{# Primary contributary cuase of pedpedal crashes #}
{{ config(materialized='table') }}

select prim_contributory_cause, crash_date
from {{ ref("stg_crashes") }}
where crash_record_id in (
    select distinct crash_record_id
    from {{ ref("pedpedal_vehicles")}}
)
