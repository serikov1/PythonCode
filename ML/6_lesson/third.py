import sklearn.datasets as f
import pandas as pd

data = f.load_iris()
# print(data)
data_pd = pd.DataFrame(data=data.data, columns=data.feature_names)
data_pd['target'] = data['target']
# print(data_pd['target'].value_counts())
mask = data_pd['target'] == 0
# print(data_pd)
data_pd.drop_duplicates(inplace=True)
# print(data_pd)

data_pd['extra'] = round((data_pd['sepal length (cm)'] + data_pd['sepal width (cm)'] + data_pd['petal length (cm)'] +
                          data_pd['petal width (cm)']) / data_pd['sepal length (cm)'], 3)

data_pd = data_pd.sort_values('extra').dropna()
print(data_pd)
print(data_pd.iloc[101, 5])

print(data_pd.groupby('target')['sepal width (cm)'].mean())