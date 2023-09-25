with source as (

    {#-
    Pulling this data from the sqlite3 db
    #}
    select * from {{ source('upstream', 'raw_customers') }}

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed
