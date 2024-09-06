import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

# Загрузка данных
# Замените 'manufacturing_data.csv' на путь к вашему файлу
data = pd.read_csv('manufacturing.csv')

# Разделение данных на обучающую и тестовую выборки
X = data.drop(columns=['Quality Rating'])  # Предполагается, что 'Quality Rating' - целевой признак
y = data['Quality Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Получение предсказаний на тренировочной и тестовой выборках
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Подсчет метрик R2 на тренировочной и тестовой выборках
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

# Округление метрик до второго знака после точки
rounded_r2_train = round(r2_train, 2)
rounded_r2_test = round(r2_test, 2)

print(f'R2 на тренировочной выборке: {rounded_r2_train}')
print(f'R2 на тестовой выборке: {rounded_r2_test}')

# Создание конвейера
pipeline = Pipeline([
    ('polynomial_features', PolynomialFeatures(degree=3)),
    ('linear_regression', LinearRegression())
])

# Обучение модели
pipeline.fit(X_train, y_train)

# Получение предсказаний на тренировочной и тестовой выборках
y_train_pred = pipeline.predict(X_train)
y_test_pred = pipeline.predict(X_test)

# Подсчет метрик R2 на тренировочной и тестовой выборках
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

# Округление метрик до второго знака после точки
rounded_r2_train = round(r2_train, 2)
rounded_r2_test = round(r2_test, 2)

print(f'R2 на тренировочной выборке: {rounded_r2_train}')
print(f'R2 на тестовой выборке: {rounded_r2_test}')