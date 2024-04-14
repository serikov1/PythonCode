import numpy as np

some_data = [
    [3, 8, 1, 0, 1, 2],
    [9, 2, 7, 3, 0, 4],
    [2, 5, 1, 3, 1, 8],
    [5, 1, 2, 1, 1, 0]
]

# далее запишите ваш код

some_data_np = np.array(some_data)
lines = some_data_np[1:]
last_column = some_data_np[:, 5]
print(last_column)
array_t = some_data_np.T
array_sum = some_data_np.sum()
array_avg = some_data_np.mean()
