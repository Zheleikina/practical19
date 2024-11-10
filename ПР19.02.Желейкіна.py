import pandas as pd
import json

with open('data.txt', 'r') as file:

    data = [list(map(int, line.split())) for line in file]

series = pd.Series([item for sublist in data for item in sublist])

unique_values = series.unique()

with open('unique_values.json', 'w') as json_file:
    json.dump(unique_values.tolist(), json_file)

print("Унікальні значення:", unique_values)
