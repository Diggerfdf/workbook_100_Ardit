import sqlite3
import pandas as pd

conn = sqlite3.connect("./Files/database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area > 2000000")
rows = cur.fetchall()
conn.close()

df =  pd.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("./Files/db_countries_2.csv", index = False)
