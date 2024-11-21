import pandas as pd

df = pd.read_csv('iris.csv')
print(df.head())

df = df.dropna()

df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

print("\nData after cleaning")
print(df.head())

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['species'] = le.fit_trasnform(df['species'])

print("\nData after transformation")
print(df.head())