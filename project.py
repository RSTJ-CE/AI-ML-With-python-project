import pandas as pd
#Predict the median salary based on university, school, anddegree
df = pd.read_csv("GraduateEmployment.csv", na_values=["na", "N.A."])

#drop na values
df = df.dropna()

#drop gross income columns
df = df.drop(columns=['employment_rate_overall','employment_rate_ft_perm','gross_monthly_mean','gross_monthly_median', 'gross_mthly_25_percentile', 'gross_mthly_75_percentile'])

#check data shapes
df.info()

#Write to cleaned csv
df.to_csv("Cleaned.csv")
