{{ config(materialized='table') }}

with source as (
      select * from {{ source('staging', 'crashes_partition') }}
),
renamed as (
    select
        {{ adapter.quote("crash_record_id") }},
        {{ adapter.quote("posted_speed_limit") }},
        {{ adapter.quote("weather_condition") }},
        {{ adapter.quote("lighting_condition") }},
        {{ adapter.quote("first_crash_type") }},
        {{ adapter.quote("trafficway_type") }},
        {{ adapter.quote("lane_cnt") }},
        {{ adapter.quote("report_type") }},
        {{ adapter.quote("crash_type") }},
        {{ adapter.quote("hit_and_run_i") }},
        {{ adapter.quote("damage") }},
        {{ adapter.quote("prim_contributory_cause") }},
        {{ adapter.quote("sec_contributory_cause") }},
        {{ adapter.quote("dooring_i") }},
        {{ adapter.quote("num_units") }},
        {{ adapter.quote("most_severe_injury") }},
        {{ adapter.quote("injuries_total") }},
        {{ adapter.quote("injuries_fatal") }},
        {{ adapter.quote("injuries_incapacitating") }},
        {{ adapter.quote("injuries_non_incapacitating") }},
        {{ adapter.quote("injuries_reported_not_evident") }},
        {{ adapter.quote("injuries_no_indication") }},
        {{ adapter.quote("injuries_unknown") }},
        {{ adapter.quote("crash_hour") }},
        {{ adapter.quote("crash_day_of_week") }},
        {{ adapter.quote("crash_month") }},
        {{ adapter.quote("latitude") }},
        {{ adapter.quote("longitude") }},
        {{ adapter.quote("location") }},
        {{ adapter.quote("crash_date") }}

    from source
)
select * from renamed
  