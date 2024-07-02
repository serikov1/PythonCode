import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Electric Car.csv')
fig = plt.figure()

x = df['TopSpeed_KmH']
y = df['PriceEuro']

plt.scatter(x, y)

fig.savefig('saved_figure.png')

labelencoder = LabelEncoder()

data_labeled = df.copy()

data_labeled.loc[:, 'BodyStyle'] = labelencoder.fit_transform(data_labeled.loc[:, 'BodyStyle'])
sum = data_labeled['BodyStyle'].sum()
cat_count = data_labeled['BodyStyle'].nunique()

print(cat_count)
print(sum)