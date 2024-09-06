import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Загрузка данных
# Замените 'your_dataset.csv' на путь к вашему файлу
data = pd.read_csv('taxi.csv')

# Разделение данных на обучающую и тестовую выборки
X = data.drop(columns=['tip_class'])  # Предполагается, что 'tip_class' - целевой признак
y = data['tip_class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Изучение масштаба данных и применение StandardScaler, если это требуется
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Обучение модели логистической регрессии
model = LogisticRegression(max_iter=400)
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

# Подсчет количества ошибочных предсказаний по каждому классу
conf_matrix = confusion_matrix(y_test, y_test_pred)
classes = model.classes_

# Подсчет процента ошибочных предсказаний по каждому классу
error_percentages = {}
for i, cls in enumerate(classes):
    true_count = conf_matrix[i, i]
    total_count = conf_matrix[i, :].sum()
    error_count = total_count - true_count
    error_percentage = (error_count / total_count) * 100
    error_percentages[cls] = round(error_percentage, 2)

# Вывод результатов
for cls, error_percentage in error_percentages.items():
    print(f'{cls}: {error_percentage}% ошибочных предсказаний')