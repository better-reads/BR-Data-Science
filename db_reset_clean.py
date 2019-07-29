import os
import sqlite3
from os.path import dirname, join

import numpy as np
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

dbname = os.environ.get('DB_NAME')
password = os.environ.get('DB_PASS') 
user = os.environ.get('DB_USER') 
host = os.environ.get('DB_HOST')

desc_info = pd.read_csv()
conn = sqlite3.connect('desc_info.sqlite3')
curs = conn.cursor()

desc_info.to_sql('desc_info', conn, if_exists='replace',
                  index_label='ind')
query = """SELECT * FROM desc_info"""

conn.execute(query)
conn.commit()

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host, port=5432)

pg_curs = pg_conn.cursor()

pg_curs.execute("DROP TABLE IF EXISTS summaries")
pg_curs.execute("DROP TABLE IF EXISTS desc_info")

create_desc_info_table = """
CREATE TABLE desc_info (
    id SERIAL PRIMARY KEY,
    title VARCHAR(400),
    description VARCHAR(30000)
)
"""

pg_curs.execute(create_desc_info_table)
pg_conn.commit()

desc_info_listed = desc_info.values.tolist()

for entry in desc_info_listed:
    entry_copy = entry
    entry_copy = tuple(entry_copy)
    insert_entry = """
    INSERT INTO desc_info
    VALUES """ + str(entry_copy)
    pg_curs.execute(insert_entry)
pg_conn.commit()
