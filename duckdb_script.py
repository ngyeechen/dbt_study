import duckdb
import pandas as pd

sql_query = '''
show tables
'''

with duckdb.connect('data/nyc_parking_violations.db') as con:
    result_df = con.sql(sql_query).df()
    print(result_df)