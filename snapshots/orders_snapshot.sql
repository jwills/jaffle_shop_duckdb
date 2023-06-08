{% snapshot orders_snapshot %}
    {{
        config(
          unique_key='order_id',
          strategy='check',
          check_cols='all',
        )
    }}
    -- Pro-Tip: Use sources in snapshots!
    select * from {{ ref('orders') }}
{% endsnapshot %}
