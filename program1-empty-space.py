import numpy as np
import matplotlib.pyplot as plt
import math
import random

def vec3(x,y,z):
    return np.array((x,y,z))

def unit_vector(v):
    len = math.sqrt(np.dot(v,v))
    return v / len

# The unit vector v returns a color that is a linear blend of light blue and dark blue depending on the y valye of v
def background_color(v):
    u = 0.5*(1.0 + v[1])
    return u*vec3(0.7, 0.8, 0.9) + (1.0-u)*vec3(0.05, 0.05, 0.2)

width = 512
height = 384
# right hand coordinate system
# z goes to me

ray_origin = vec3(0, 0, 0)
aspect = height / width
window_depth = 2.0

im = np.random.random(size=(height, width, 3))
# u, v - fraction of the screen
# (0, 1)
# 0 - you are on the far left
# 0.5 you are at the middle
# 1 you are at the right
for row in range(height):
    for column in range(width):
        u = (column + 0.5) / width
        v = (row + 0.5) / height
        # normalize to (-1, 1)
        point_on_the_window = vec3(2.0*u - 1.0, 2.0*v -1.0, -window_depth)
        ray_direction = unit_vector(point_on_the_window)
        im[row,column,:] = background_color(ray_direction)

im = im * im
plt.imshow(im)
plt.show()