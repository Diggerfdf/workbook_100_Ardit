import sqlite3
import pandas as pd

conn = sqlite3.connect("./Files/database.db")

df_r = pd.read_sql('''SELECT * FROM countries WHERE area > 2000000''', conn)

conn.close()

# print(df_r['country'])

for i in df_r['country']:
    print(i)