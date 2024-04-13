{# Count the different combos of vehicles involved in each pedpedal crash, by month #}
{{ config(materialized='table') }}

{# select unit_types as `Vechicles Involved`, count(*) as Count, crash_month
from
(select crash_record_id, string_agg(unit_type, "," order by unit_type asc) as unit_types, {{ dbt.date_trunc("month", "crash_date") }} as crash_month
from {{ ref("pedpedal_vehicles") }}
group by crash_record_id, crash_date) as crashes
group by unit_types, crash_month #}

select unit_types as vehicles_involved, crash_month
from
(select crash_record_id, string_agg(unit_type, ", " order by unit_type asc) as unit_types, {{ dbt.date_trunc("month", "crash_date") }} as crash_month
from {{ ref("pedpedal_vehicles") }}
group by crash_record_id, crash_date) as crashes