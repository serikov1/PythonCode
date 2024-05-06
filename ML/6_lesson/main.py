# начальный код

import random
import pandas as pd

random.seed(10)

list_metrics = []

for i in range(0,300):
  n = random.randint(-100,1000)
  list_metrics.append(n)

list_metrics = pd.DataFrame({'Прирост': list_metrics})
list_metrics

# далее будет код шаблона
result1 = round(list_metrics['Прирост'].std(), 2)
result2 = round(list_metrics['Прирост'].max() - list_metrics['Прирост'].mean(), 2)
print(result1, result2)
