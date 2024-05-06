import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Electric_Car.csv")

cars_models = df.groupby(['Brand'])['Model'].count().sort_values(ascending=False)

bar_chart = plt.barh(cars_models.index, cars_models.values)
plt.title('Количество моделей определнного бренда')
plt.grid()
plt.savefig('saved_figure_barh.png')
plt.show()
