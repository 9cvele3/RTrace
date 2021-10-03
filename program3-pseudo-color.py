import numpy as np
import matplotlib.pyplot as plt
import math
import random
from utils import *

# map unit vector (-1, 1)
# to rgb color (0,1)
def pseudocolor(v):
    return 0.5 * (vec3(1,1,1) + v)

width = 512
height = width

ray_origin = vec3(0, 0, 0)
aspect = height / width
window_depth = 2.0

im = np.random.random(size=(height, width, 3))

sphere_centers = [vec3(0, 0, -10)]
sphere_radii = [3.0]

for row in range(height):
   if (row % 50 == 0):
       print ('row = ', row)

   for column in range(width):
        u = (column + 0.5) / width
        v = (row + 0.5) / height
        point_on_the_window = vec3(2.0*u - 1.0, 2.0*v -1.0, -window_depth)
        ray_direction = unit_vector(point_on_the_window)

        t = hit_sphere(ray_origin, ray_direction, sphere_centers[0], sphere_radii[0])

        if t < 1.0e8:
            hit_point = ray_origin + t * ray_direction
            surface_normal = (1 / sphere_radii[0])*(hit_point - sphere_centers[0])
            im[row,column,:] = pseudocolor(surface_normal)
        else:
            im[row,column,:] = background_color(ray_direction)

im = im * im
plt.imshow(im)
plt.show()
