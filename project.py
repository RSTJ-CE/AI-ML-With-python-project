import pandas as pd

df = pd.read_csv("GraduateEmployment.csv")
df = df.dropna()

df.to_csv("Cleaned.csv")
