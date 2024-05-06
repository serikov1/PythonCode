import pandas as pd

police = pd.read_csv("police.csv", sep=',')

# print(police.isnull().sum())

mask = (police['driver_gender'] == 'M')

print(mask)

police.drop(['county_name'], inplace=True, axis=1)


