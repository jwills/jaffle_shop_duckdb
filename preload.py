import sqlite3
import pandas as pd

# CSV file paths
file1 = 'preseeds/raw_customers.csv'
file2 = 'preseeds/raw_payments.csv'
file3 = 'preseeds/raw_orders.csv'

# Create a new SQLite connection (or connect to an existing database)
conn = sqlite3.connect('seeds.sqlite3')

try:
    # Read CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.read_csv(file3)

    # Write DataFrames to SQLite tables
    df1.to_sql('raw_customers', conn, index=False, if_exists='replace')
    df2.to_sql('raw_payments', conn, index=False, if_exists='replace')
    df3.to_sql('raw_orders', conn, index=False, if_exists='replace')

finally:
    # Close the SQLite connection
    conn.close()

print("Data has been successfully ingested into SQLite.")
