
# 

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
    [0.2, 4],
    [4, 4],
    [4, 2.5],
    [4, 2.5],
    [0.2, 1.0],
    [2.0, 4],
    [4, 1],
    [0.2, 2.5],
    [1.0, 2.5],
    [2.0, 1.0]
])

""" 
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color = "#2298e7")

plt.show()
"""
hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1], color = "r")
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-',)

plt.suptitle("CONVEXHULL", color = "r")
plt.show()


