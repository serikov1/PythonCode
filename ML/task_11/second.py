import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Загрузка данных
# Замените 'student-mat.csv' на путь к вашему файлу
data = pd.read_csv('student.csv')

# Преобразование целевого признака grade в бинарный формат
data['grade'] = data['grade'].apply(lambda x: 1 if x >= data['grade'].mean() else 0)

# Разделение данных на обучающую и тестовую выборки
X = data.drop(columns=['grade'])  # Предполагается, что 'grade' - исходный целевой признак
y = data['grade']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Создание пайплайна
pipeline = Pipeline([
    ('polynomial_features', PolynomialFeatures(degree=4)),
    ('scaler', StandardScaler()),
    ('logistic_regression', LogisticRegression(penalty=None, max_iter=1000))
])

# Обучение пайплайна на тренировочной выборке
pipeline.fit(X_train, y_train)

# Получение предсказаний на тренировочной и тестовой выборках
y_train_pred = pipeline.predict(X_train)
y_test_pred = pipeline.predict(X_test)

# Подсчет метрики accuracy на тренировочной и тестовой выборках
accuracy_train = accuracy_score(y_train, y_train_pred)
accuracy_test = accuracy_score(y_test, y_test_pred)

# Округление метрик до второго знака после точки
rounded_accuracy_train = round(accuracy_train, 2)
rounded_accuracy_test = round(accuracy_test, 2)

print(f'Accuracy на тренировочной выборке: {rounded_accuracy_train}')
print(f'Accuracy на тестовой выборке: {rounded_accuracy_test}')
print(f'{rounded_accuracy_train} {rounded_accuracy_test}')

# Список значений для параметра C
C_values = [0.0001, 0.001, 0.01, 0.1, 1]

# Перебор параметра C
best_accuracy = 0
best_C = None

for C in C_values:
    # Создание пайплайна
    pipeline = Pipeline([
        ('polynomial_features', PolynomialFeatures(degree=4)),
        ('scaler', StandardScaler()),
        ('logistic_regression', LogisticRegression(penalty='l2', C=C, max_iter=600))
    ])

    # Обучение пайплайна на тренировочной выборке
    pipeline.fit(X_train, y_train)

    # Получение предсказаний на тестовой выборке
    y_test_pred = pipeline.predict(X_test)

    # Подсчет метрики accuracy на тестовой выборке
    accuracy_test = accuracy_score(y_test, y_test_pred)

    # Обновление лучшей метрики
    if accuracy_test > best_accuracy:
        best_accuracy = accuracy_test
        best_C = C

# Округление лучшей метрики до второго знака после точки
rounded_best_accuracy = round(best_accuracy, 2)

print(f'Самая лучшая метрика accuracy на тесте: {rounded_best_accuracy} при C = {best_C}')
