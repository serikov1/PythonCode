import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
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

# Обучение модели логистической регрессии
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Получение веса для признака studytime
coefficient = model.coef_[0][X.columns.get_loc('studytime')]

# Округление веса до второго знака после точки
rounded_coefficient = round(coefficient, 2)

print(f'Вес для признака studytime: {rounded_coefficient}')

# Обучение модели StandardScaler на тренировочной выборке
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Преобразование обратно в DataFrame для удобства
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Получение минимального и максимального значений признака age на тестовой выборке после стандартизации
age_min = X_test_scaled['age'].min()
age_max = X_test_scaled['age'].max()

print(f'Минимальное значение признака age: {age_min}')
print(f'Максимальное значение признака age: {age_max}')
print(f'Диапазон значений признака age: {age_min} {age_max}')

# Обучение модели логистической регрессии на стандартизованных данных
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Получение предсказаний на тренировочной и тестовой выборках
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Подсчет метрики accuracy на тренировочной и тестовой выборках
accuracy_train = accuracy_score(y_train, y_train_pred)
accuracy_test = accuracy_score(y_test, y_test_pred)

# Округление метрик до второго знака после точки
rounded_accuracy_train = round(accuracy_train, 2)
rounded_accuracy_test = round(accuracy_test, 2)

print(f'Accuracy на тренировочной выборке: {rounded_accuracy_train}')
print(f'Accuracy на тестовой выборке: {rounded_accuracy_test}')
print(f'{rounded_accuracy_train} {rounded_accuracy_test}')