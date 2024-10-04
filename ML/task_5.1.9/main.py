import pandas as pd
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier

# 1. Считать данные через pandas
data = pd.read_csv("light_music.csv")

# 2. Разделить данные на обучающую и тестовую выборки
X = data.drop(columns=['popularity'])  # Предполагается, что 'popularity' - целевой признак
y = data['popularity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 3. Проверить наличие категориальных строковых признаков и преобразовать их через OrdinalEncoder
categorical_columns = X.select_dtypes(include=['object']).columns
if not categorical_columns.empty:
    encoder = OrdinalEncoder()
    X_train[categorical_columns] = encoder.fit_transform(X_train[categorical_columns])
    X_test[categorical_columns] = encoder.transform(X_test[categorical_columns])

# 4. Определить размерность тренировочной и тестовой выборок
train_shape = X_train.shape
test_shape = X_test.shape

print(f'Размерность тренировочной выборки: {train_shape[0]}, {train_shape[1]}')
print(f'Размерность тестовой выборки: {test_shape[0]}, {test_shape[1]}')

# 4. Обучить дерево решений для задачи на базовых параметрах с фиксированным random_state=1
model = DecisionTreeRegressor(random_state=1)
model.fit(X_train, y_train)

# 5. Посчитать метрику MSE (Mean Squared Error)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f'MSE: {mse:.2f}')

# 4. Обучить дерево решений для задачи на базовых параметрах с фиксированным random_state=1, изменяя глубину дерева в диапазоне от 1 до 25
best_mse = float('inf')
best_depth = None

for depth in range(1, 26):
    model = DecisionTreeRegressor(max_depth=depth, random_state=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    if mse < best_mse:
        best_mse = mse
        best_depth = depth

# 5. Вывести лучшее значение метрики MSE, округленное до 2 знака после точки
print(f'Лучшая глубина дерева: {best_depth}')
print(f'Лучшее значение MSE: {best_mse:.2f}')

# 4. Перевести целевой признак `popularity` в бинарный вид
y_train_bin = (y_train > 50).astype(int)
y_test_bin = (y_test > 50).astype(int)

# 5. Посчитать соотношение классов на обучающей и тестовой выборках
train_class_ratio = y_train_bin.value_counts(normalize=True)
test_class_ratio = y_test_bin.value_counts(normalize=True)

print(f'Соотношение классов на обучающей выборке: {train_class_ratio}')
print(f'Соотношение классов на тестовой выборке: {test_class_ratio}')

best_accuracy = 0
best_depth = None

for depth in range(1, 26):
    model = DecisionTreeClassifier(max_depth=depth, random_state=1)
    model.fit(X_train, y_train_bin)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test_bin, y_pred)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_depth = depth

# 6. Вывести лучшее значение метрики accuracy, округленное до 2 знака после точки
print(f'Лучшая глубина дерева: {best_depth}')
print(f'Лучшее значение accuracy: {best_accuracy:.2f}')

# 5. Обучить дерево решений для задачи бинарной классификации с фиксированным random_state=1, изменяя глубину дерева в диапазоне от 1 до 25
best_accuracy = 0
best_depth = None
best_model = None

for depth in range(1, 26):
    model = DecisionTreeClassifier(max_depth=depth, random_state=1)
    model.fit(X_train, y_train_bin)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test_bin, y_pred)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_depth = depth
        best_model = model

# 6. Получить важности признаков у обученной модели дерева решений
feature_importances = best_model.feature_importances_

# 7. Вывести важности признаков
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

print(f'Лучшая глубина дерева: {best_depth}')
print(f'Лучшее значение accuracy: {best_accuracy:.2f}')
print('Важности признаков:')
print(importance_df)