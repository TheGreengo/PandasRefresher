import pandas as pd

df = pd.read_csv("example.csv")

print(df)
print(df['age'])
print(df['age'][2])
print(df)
df.to_csv("example.csv")
