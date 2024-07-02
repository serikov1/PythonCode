import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('supermarket.csv', sep=',')

# Приведение полей Date и Time к типу datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'])

# Вывод наличия пропусков в датасете
missing_values = df.isnull().sum() / len(df) * 100
missing_values = missing_values.sort_values(ascending=False)
print(missing_values)

# Вычисление общего дохода по городам
city_income = df.groupby('City')['gross income'].sum()
print('Общий доход по городам:')
print(city_income)

# Вычисление общего дохода по датам
date_income = df.groupby('Date')['gross income'].sum()

# Вычисление суммарного дохода по каждому магазину
store_income = df.groupby(['City', 'Date'])['gross income'].sum().unstack().fillna(0)

# Построение графика
# fig, ax = plt.subplots(figsize=(12, 6))
# ax.stackplot(store_income.index, store_income.values, labels=store_income.columns)
# ax.set_xlabel('Дата')
# ax.set_ylabel('Суммарный доход')
# ax.legend(loc='upper left')
# plt.show()

product = df.groupby('Product line')['Quantity'].sum()
print(product)