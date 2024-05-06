import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Electric_Car.csv")

cars_count = df['Brand'].value_counts().sort_values(ascending=False)
print(cars_count)

rest_count = cars_count[cars_count < 6].sum()
main_brands = cars_count[cars_count >= 6]
main_brands['Rest'] = rest_count

plt.figure(figsize=(8, 8))
pie_chart = plt.pie(main_brands, labels=main_brands.index, autopct="%1.1f%%", radius=2)
plt.savefig('auto_pie.png')

for p, t, a in zip(*pie_chart):
    print(p.r, round(p.theta1, 4), t.get_text(), a.get_text())

plt.show()