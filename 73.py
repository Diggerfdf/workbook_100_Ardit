import pandas as pd

df = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")

df_x_2 = df * 2

df_x_2.to_csv('./Files/73.txt', index = False)