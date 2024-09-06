import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

# Загрузка данных
csv = 'poly.csv'
data = pd.read_csv(csv)

# Разделение данных на обучающую и тестовую выборки
X = data[['X']]
y = data['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Получение предсказаний на тестовых и тренировочных объектах
y_pred_test = model.predict(X_test)
y_pred_train = model.predict(X_train)

# Подсчет метрик R2
r2_test = r2_score(y_test, y_pred_test)
r2_train = r2_score(y_train, y_pred_train)

# Округление метрик до второго знака после точки
rounded_r2_test = round(r2_test, 2)
rounded_r2_train = round(r2_train, 2)

print(f'R2_test: {rounded_r2_test}')
print(f'R2_train: {rounded_r2_train}')

# Перебор параметра degree в диапазоне от 2 до 7
worst_r2_test = float('inf')
worst_degree = None

for degree in range(2, 8):
    # Создание конвейера
    pipeline = Pipeline([
        ('polynomial_features', PolynomialFeatures(degree=degree)),
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

    print(f'Degree: {degree}')
    print(f'R2 на тренировочной выборке: {rounded_r2_train}')
    print(f'R2 на тестовой выборке: {rounded_r2_test}')

    # Обновление самой плохой метрики
    if rounded_r2_test < worst_r2_test:
        worst_r2_test = rounded_r2_test
        worst_degree = degree

print(f'Самая плохая метрика R2 на тестовом датасете: {worst_r2_test} при degree = {worst_degree}')

# Перебор параметра alpha в диапазоне от 0 до 10
best_r2_test = float('-inf')
best_alpha = None

for alpha in range(0, 11):
    # Создание конвейера
    pipeline = Pipeline([
        ('polynomial_features', PolynomialFeatures(degree=7)),
        ('ridge_regression', Ridge(alpha=alpha))
    ])

    # Обучение модели
    pipeline.fit(X_train, y_train)

    # Получение предсказаний на тренировочной и тестовой выборках
    y_train_pred = pipeline.predict(X_train)
    y_test_pred = pipeline.predict(X_test)

    # Подсчет метрик R2 на тренировочной и тестовой выборках
    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)

    # Округление метрик до трех знаков после точки
    rounded_r2_train = round(r2_train, 3)
    rounded_r2_test = round(r2_test, 3)

    print(f'Alpha: {alpha}')
    print(f'R2 на тренировочной выборке: {rounded_r2_train}')
    print(f'R2 на тестовой выборке: {rounded_r2_test}')

    # Обновление самой лучшей метрики
    if rounded_r2_test > best_r2_test:
        best_r2_test = rounded_r2_test
        best_alpha = alpha

print(f'Самая лучшая метрика R2 на тестовой выборке: {best_r2_test} при alpha = {best_alpha}')