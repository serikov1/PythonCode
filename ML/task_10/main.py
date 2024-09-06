import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Загрузка данных
csv = 'Salary_dataset.csv'
data = pd.read_csv(csv)

# Разделение данных на обучающую и тестовую выборки
X = data[['YearsExperience']]
y = data['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Получение веса для признака YearsExperience
coefficient = model.coef_[0]

# Округление веса до второго знака после точки
rounded_coefficient = round(coefficient, 2)

print(f'Вес для признака YearsExperience: {rounded_coefficient}')

# Получение предсказаний на тестовых объектах
y_pred = model.predict(X_test)

# Подсчет метрик MAE и R2
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Округление метрик до второго знака после точки
rounded_mae = round(mae, 2)
rounded_r2 = round(r2, 2)

print(f'MAE: {rounded_mae}')
print(f'R2: {rounded_r2}')
