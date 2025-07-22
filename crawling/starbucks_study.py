import pandas as pd 

df = pd.read_csv("C:\AI_SW\starbucks_seoul.csv")
# print(df.info())
pd.set_option('display.max_columns', 4)
print(df.head())
