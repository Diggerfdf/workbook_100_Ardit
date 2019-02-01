import sqlite3
import pandas as pd

data = pd.read_csv("./Files/ten-more-countries.txt")

conn = sqlite3.connect("./Files/database.db")
cur = conn.cursor()

for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES(NULL,?,?,NULL)",(row["Country"], row["Area"]))
conn.commit()
conn.close()

'''
import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
df = pd.read_csv('ten-more-countries.txt')
df.to_sql('countries',conn, if_exists='append', index=False)]
'''
