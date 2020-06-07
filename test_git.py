import pandas as pd


df = pd.read_csv('pix.csv')
print(df.head())

df1 = pd.read_csv('pix.csv')
print(df1.head())

assert df = df1
