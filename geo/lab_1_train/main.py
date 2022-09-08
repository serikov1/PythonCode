import numpy as np
import matplotlib.pyplot as plt
from pyorbital.orbital import Orbital

from datetime import datetime, timedelta

start = datetime(2022, 3, 4, 18, 29, 18)
end = datetime(2022, 3, 5, 18, 29, 18)
print(
    "Интересуемый диапазон: c {} до {}".format(start.strftime("%d.%m.%Y %H:%M:%S"), end.strftime("%d.%m.%Y %H:%M:%S")))

tle_0 = "NOAA 19"
tle_1 = "1 33591U 09005A   22083.34999260  .00000090  00000-0  73903-4 0  9997"
tle_2 = "2 33591  99.1591 115.6572 0014777  69.0998 291.1753 14.12540211676436"

# Координаты ЛК
obs_lat, obs_long, obs_h = 55.75, 37.62, 100

# Получаем актуальный tle
orb = Orbital(tle_0)

# Получаем положение аппарата в заданном временном диапазоне
ecis = []
for i in range(1440):
    ecis.append(orb.get_position(start + i * timedelta(minutes=1), normalize=False)[0])

# Получаем прогноз видимости аппарата для антенны-наблюдателя
begin = []
finish = []
for minute in range(1440):
    if orb.get_observer_look(start + minute * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] > 0:
        if orb.get_observer_look(start + (minute - 1) * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] < 0:
            begin.append(start + minute * timedelta(minutes=1))
        if orb.get_observer_look(start + (minute + 1) * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] < 0:
            finish.append(start + minute * timedelta(minutes=1))
for elem in range(len(begin)):
    print("Диапазон когда спутник виден: c {} до {}".format(begin[elem].strftime("%d.%m.%Y %H:%M:%S"),
                                                            finish[elem].strftime("%d.%m.%Y %H:%M:%S")))

# В промежутки времени, когда аппарат «виден» для антенны, посчитаем
# требуемые для связи углы азимута и элевации в каждый момент времени
azimut = []
elevation = []
radius = []
angle = []
for i in range(1440):
    if orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] > 0:
        azimut.append(orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, obs_h)[0])
        elevation.append(orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1])
        if orb.get_observer_look(start + (i + 1) * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] < 0:
            r = np.array(elevation)
            c = np.array(azimut)
            radius.append(r)
            angle.append(c * np.pi / 180)
            azimut.clear()
            elevation.clear()


# График в полярных координатах
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for i in range(len(radius)):
    ax.plot(angle[i], (radius[i]), color='blue')
ax.grid(True)
ax.set_theta_offset(np.pi / 2.0)
ax.set_rmax(0)
ax.set_rmin(90)
ax.set_rticks([90, 60, 30, 0])
plt.show()
