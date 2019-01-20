import pandas as pd

df = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
df_2 = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

df_f = pd.concat([df, df_2])

df_f.to_csv('./Files/74.txt', index = False)