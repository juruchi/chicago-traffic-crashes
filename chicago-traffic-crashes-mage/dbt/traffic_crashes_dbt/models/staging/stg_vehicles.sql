{{ config(materialized='table') }}

with source as (
      select * from {{ source('staging', 'vehicles_partition') }}
),
renamed as (
    select
        {{ adapter.quote("crash_unit_id") }},
        {{ adapter.quote("crash_record_id") }},
        {{ adapter.quote("unit_no") }},
        {{ adapter.quote("unit_type") }},
        {{ adapter.quote("exceed_speed_limit_i") }},
        {{ adapter.quote("crash_date") }}

    from source
)
select * from renamed
  