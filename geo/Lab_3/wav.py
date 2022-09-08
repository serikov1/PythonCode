import matplotlib.pyplot as plt
import cv2
import shapefile
from scipy import interpolate
import numpy as np
from pyorbital.orbital import Orbital
from datetime import datetime
from pyproj import Transformer
from skyfield.api import load, wgs84

tle = "NOAA 19"
us_lat, us_long, us_h = 55.75, 37.62, 100
orb = Orbital(tle)
print(orb)

time_begin = datetime(2022, 4, 18, 18, 30, 14)
time_end = datetime(2022, 4, 18, 18, 37, 12)

start_latlon = orb.get_lonlatalt(time_begin)[:-1]
end_latlon = orb.get_lonlatalt(time_end)[:-1]
print(np.roll(start_latlon, 1))
print(np.roll(end_latlon, 1))

start_latlon = [elem * np.pi / 180 for elem in start_latlon]
start_latlon = np.roll(start_latlon, 1)
end_latlon = [elem * np.pi / 180 for elem in end_latlon]
end_latlon = np.roll(end_latlon, 1)
print(start_latlon)
print(end_latlon)

# Получаю координаты в нужной системе отсчета
transformer = Transformer.from_crs(4326, 3857)
points = [(-40.905479, 25.2152624), (-16.62773305, 18.23607705)]
for pt in transformer.itransform(points): print('{:.3f} {:.3f}'.format(*pt))

# Раскраска фото
palett = cv2.imread('palett2.png')
photo = cv2.imread('photo_2.png')

for i in range(0, 833):
    for j in range(0, 5390 - 2980):
        photo[i][j + 226] = palett[photo[i][j + 226][0]][photo[i][j + 2980][0]]


# plt.imshow(photo, cmap='gray')
# plt.axis('off')
# plt.savefig('photo_2.png', bbox_inches='tight', pad_inches=0, dpi=1111)
# plt.title('Image')
# plt.savefig('col_photo.png')
# plt.show()

#  Функция для построения границ
def draw(img):
    yaw = 0.
    vscale = 1
    hscale = 1

    # Compute the great-circle distance between two points
    # The units of all input and output parameters are radians
    def distance(lat1, lon1, lat2, lon2):
        # https://en.wikipedia.org/w/index.php?title=Great-circle_distance&oldid=749078136#Computational_formulas

        delta_lon = lon2 - lon1

        cos_central_angle = np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(delta_lon)

        if cos_central_angle < -1:
            cos_central_angle = -1

        if cos_central_angle > 1:
            cos_central_angle = 1

        return np.arccos(cos_central_angle)

    height = len(img)

    y_res = distance(*start_latlon, *end_latlon) / height / vscale
    x_res = 0.0005 / hscale

    # Compute azimuth of line between two points
    # The angle between the line segment defined by the points (`lat1`,`lon1`) and (`lat2`,`lon2`) and the North
    # The units of all input and output parameters are radians
    def azimuth(lat1, lon1, lat2, lon2):
        # https://en.wikipedia.org/w/index.php?title=Azimuth&oldid=750059816#Calculating_azimuth

        delta_lon = lon2 - lon1

        return np.arctan2(np.sin(delta_lon), np.cos(lat1) * np.tan(lat2) - np.sin(lat1) * np.cos(delta_lon))

    ref_az = azimuth(*start_latlon, *end_latlon)

    def latlon_to_rel_px(latlon):
        az = azimuth(*start_latlon, *latlon)
        B = az - ref_az

        c = distance(*latlon, *start_latlon)

        if c < -np.pi / 3:
            c = -np.pi / 3

        if c > np.pi / 3:
            c = np.pi / 3

        a = np.arctan(np.cos(B) * np.tan(c))
        b = np.arcsin(np.sin(B) * np.sin(c))

        x = -b / x_res

        # Add the yaw correction value
        # Should be calculating sin(yaw) * x but yaw is always a small value
        y = a / y_res + yaw * x

        return (x, y)

    def draw_line(latlon1, latlon2, r, g, b, a):
        # Convert latlon to (x, y)
        (x1, y1) = latlon_to_rel_px(latlon1)
        (x2, y2) = latlon_to_rel_px(latlon2)

        f = interpolate.interp1d((x1, x2), (y1, y2))
        xar = np.arange(x1, x2)
        dlimg = len(img[0]) / 2080
        bounds_1 = int(dlimg * 456)  # 456
        bounds_2 = int(dlimg * 600)  # 600
        shift_1 = int(dlimg * 539)  # 539
        shift_2 = int(dlimg * 1579)  # 1579
        if (x1 > -bounds_1 and x1 < bounds_1 and y1 > 0. and y1 < height) or (
                x1 > -bounds_2 and x1 < bounds_2 and y1 > 0. and y1 < height):
            for x in xar:
                y = f(x)
                if x > -bounds_1 and x < bounds_1 and y > 0 and y < height:
                    img[int(y), int(x) + shift_1] = [r, g, b]
                    img[int(y), int(x) + shift_2] = [r, g, b]

    def draw_shape(shpfile, r, g, b):
        reader = shapefile.Reader(shpfile)
        for shape in reader.shapes():
            prev_pt = shape.points[0]
            for pt in shape.points:
                draw_line(
                    (pt[1] / 180. * np.pi, pt[0] / 180. * np.pi),
                    (prev_pt[1] / 180. * np.pi, prev_pt[0] / 180. * np.pi),
                    r, g, b, 0
                )
                prev_pt = pt

    draw_shape(
        "https://github.com/nvkelso/natural-earth-vector/blob/master/10m_cultural/ne_10m_admin_0_countries.shp?raw=true",
        255, 255, 0)
    return img


# Сохраняю фото с границами
plt.axis('off')
plt.imshow(draw(photo), cmap='gray')
# plt.savefig('borders_1', bbox_inches='tight', pad_inches=0, dpi=1111)
plt.show()


# Подгружаю полученное фото в нужном формате
photo_1 = cv2.imread('borders_1.png')


# Вырезаю нужный кусок
pict_new = []
for i in range(0, 833):
    for j in range(2635 - 226):
        pict_new.append(photo_1[i][j + 226])


#  Делаю матрицу из массива pict_new
pict = []
for i in range(833):
    p = pict_new[i * 2409: (i + 1) * 2409]
    pict.append(p)

# Сохраняю в нужном разрешении
# plt.axis('off')
# plt.imshow(pict,  cmap='gray')
# # plt.savefig('result', bbox_inches='tight', pad_inches=0, dpi=486)
# plt.show()
