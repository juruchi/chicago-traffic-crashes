{{ config(materialized='table') }}

with source as (
      select * from {{ source('staging', 'people_partition') }}
),
renamed as (
    select
        {{ adapter.quote("person_id") }},
        {{ adapter.quote("person_type") }},
        {{ adapter.quote("crash_record_id") }},
        {{ adapter.quote("vehicle_id") }},
        {{ adapter.quote("sex") }},
        {{ adapter.quote("age") }},
        {{ adapter.quote("injury_classification") }},
        {{ adapter.quote("driver_action") }},
        {{ adapter.quote("pedpedal_action") }},
        {{ adapter.quote("cell_phone_use") }},
        {{ adapter.quote("crash_date") }}

    from source
)
select * from renamed
  