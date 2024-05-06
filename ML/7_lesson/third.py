import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from scipy import spatial
from stl import mesh


#
# # Функция отображения вершин
# def plot_verticles(vertices, isosurf=False, filename=None):
#     # Создание новой графики
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     x = [v[0] for v in vertices]
#     y = [v[1] for v in vertices]
#     z = [v[2] for v in vertices]
#     if isosurf:
#         ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
#     else:
#         ax.scatter(x, y, z, c='r', marker='o')
#         ax.set_xlabel('X')
#         ax.set_ylabel('Y')
#         ax.set_zlabel('Z')
#     # Отображение файла или запись файла
#     if filename is None:
#         plt.show()
#     else:
#         plt.savefig(filename)
#
#
def plot_mesh(your_mesh, size_x=10, size_y=10, dpi=80, filename=None):
    # Создание нового 3D отображения
    figure = plt.figure(figsize=(size_x, size_y), dpi=dpi)
    # axes = mplot3d.Axes3D(figure, auto_add_to_figure=False)
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors, edgecolor="black"))
    figure.add_axes(axes)
    # Auto scale к размеру сетки
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    # Отображение и запись графика
    if filename is None:
        plt.show()
    else:
        # matplotlib.use('Agg')
        plt.savefig(filename)


def create_sphere(cx, cy, cz, r, resolution=36):
    resolution = 36
    phi = np.linspace(0, 2 * np.pi, 2 * resolution)
    theta = np.linspace(0, np.pi, resolution)
    r = 1
    cx = 1
    cy = 1
    cz = 1
    vertices_ = np.empty([0, 3])
    for p in phi:
        for t in theta:
            r_xy = r * np.sin(t)
            x = cx + np.cos(p) * r_xy
            y = cy + np.sin(p) * r_xy
            z = cz + r * np.cos(t)
            vertices_ = np.append(vertices_, [[x, y, z]], axis=0)
    return vertices_


vertices = create_sphere(1, 1, 1, 1, resolution=36)

hull = spatial.ConvexHull(vertices)
faces = hull.simplices  # Массив faces содержит описание граней

myramid_mesh = mesh.Mesh(np.zeros(faces.shape[0],
                                  dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        myramid_mesh.vectors[i][j] = vertices[f[j], :]

plot_mesh(myramid_mesh)
