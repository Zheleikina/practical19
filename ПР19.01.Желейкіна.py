from numpy import *
import pandas as pd

df = pd.read_csv('weight.csv')

print(df.head())

df['total_weight'] = df['capacity'] * df['trips']

df.to_csv('auto.csv', index=False)

print(df[['capacity', 'trips', 'total_weight']])
