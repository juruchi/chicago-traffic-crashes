{# Number of pedpedal crashes throughout time #}
{{ config(materialized='table') }}

select count(crash_record_id) as monthly_crashes, {{ dbt.date_trunc("month", "crash_date") }} as crash_month
from {{ ref("stg_crashes") }}
where crash_record_id in (
    select distinct crash_record_id
    from {{ ref("pedpedal_vehicles")}}
)
group by crash_month
order by crash_month
