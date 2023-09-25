-- illustrates calling a plugin-defined UDF ("foo") inside of a SQL-based dbt model
SELECT foo() as foo_value
