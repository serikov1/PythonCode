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

# observer coordinates in degrees
obs_lat, obs_long, obs_h = 55.75, 37.62, 100

orb = Orbital(tle_0)
ecis = []
for i in range(1440):
    ecis.append(orb.get_position(start + i * timedelta(minutes=1), normalize=False)[0])

# obs_look = []
step = 1440
begin = []
finish = []
for min in range(step):
    if orb.get_observer_look(start + min * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] > 0:
        if orb.get_observer_look(start + (min - 1) * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] < 0:
            begin.append(start + min * timedelta(minutes=1))
        if orb.get_observer_look(start + (min + 1) * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] < 0:
            finish.append(start + min * timedelta(minutes=1))
for elem in range(len(begin)):
    print("Диапазон когда спутник виден: c {} до {}".format(begin[elem].strftime("%d.%m.%Y %H:%M:%S"),
                                                            finish[elem].strftime("%d.%m.%Y %H:%M:%S")))

azimut = []
elevation = []
radius = []
corner = []
for i in range(step):
    if orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] > 0:
        azimut.append(orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, obs_h)[0])
        elevation.append(orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1])
        if orb.get_observer_look(start + (i + 1) * timedelta(minutes=1), obs_long, obs_lat, obs_h)[1] < 0:
            r = np.array(elevation)
            c = np.array(azimut)
            radius.append(90 - r)
            corner.append(c * np.pi / 180)
            azimut.clear()
            elevation.clear()

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for i in range(len(radius)):
    ax.plot(corner[i], (90 - radius[i]), color='blue')
ax.grid(True)
ax.set_theta_offset(np.pi / 2.0)
ax.set_rmax(0)
ax.set_rmin(90)
ax.set_rticks([90, 60, 30, 0])
