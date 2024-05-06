import numpy as np
from scipy import spatial

N = 20  # Number of angular sectors

# 1. Generate vertices for the bottom base
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
bottom_base = np.column_stack((np.zeros(N), np.cos(theta), np.sin(theta)))

# 2. Generate vertices for the top base (height = 1)
top_base = np.column_stack((np.ones(N), np.cos(theta), np.sin(theta)))

# 3. Combine vertices and create faces
vertices = np.concatenate((bottom_base, top_base))

# Generate faces for the top and bottom
bottom_faces = np.arange(N).reshape(N, 1)
top_faces = (np.arange(N) + N).reshape(N, 1)

# Generate faces for the sides
lateral_faces = np.column_stack((
    np.arange(N), np.arange(N) + N, (np.arange(N) + 1) % N + N, (np.arange(N) + 1) % N
))

faces = np.concatenate((bottom_faces, top_faces, lateral_faces))

# 4. Create a mesh object
mesh = spatial.Delaunay(vertices)

# 5. Visualize the cylinder (requires matplotlib)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(vertices[:,0], vertices[:,1], vertices[:,2], triangles=faces)
plt.show()

# 6. Save the mesh as an STL file
from stl import mesh as stl_mesh

# Create the STL mesh object
stl_mesh_obj = stl_mesh.Mesh(np.zeros(faces.shape[0], dtype=stl_mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        stl_mesh_obj.vectors[i][j] = vertices[face[j],:]

# Write the STL file
stl_mesh_obj.save('cylinder.stl')