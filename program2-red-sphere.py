import numpy as np
import matplotlib.pyplot as plt
import math
import random
from utils import *

# The implicit equation for a sphere with origin at center is 
#    f(x,y,z) = x^2 + y^2 + z^2 - R^2 = 0 
# In vector form, for 3D points p = (x,y,z) on sphere that is: 
#    f(p) = dot(p,p) - R^2 = 0 
# When the center is at c = (cx, cy, cz) the implict equation for points on the sphere is: 
#    f(p) = dot(p-c,p-c) - R^2 = 0
# For a ray p(t) = o + t*v, it will be on the sphere (so "hit" it) when f(p(t)) = 0
#    dot(o + t*v - c,o + t*v - c) - R^2 = 0
#    dot(o-c,o-c) 2*t*dot(o-c,v) + t^2*dot(v,v) - R^2 = 0
# We can write that as At^2 + Bt + C = 0 and solve the quadratic for t
# If the ray missed the sphere there is no real solution (the discriminant is negative)
# If two solutions, take the smallter that is positive (negative hits are "behind" you)
def hit_sphere(ray_origin, ray_direction, center, radius):
    oc = ray_origin - center
    qb = np.dot(oc,ray_direction)
    qc = np.dot(oc,oc)-radius*radius
    discriminant = qb*qb-qc
    if (discriminant > 0):
        t = (-qb - math.sqrt(discriminant))
        if t > 0.00001:
            return t
        t = (-qb + math.sqrt(discriminant))
        if t > 0.0001:
            return t
    return 1.0e9

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

        if hit_sphere(ray_origin, ray_direction, sphere_centers[0], sphere_radii[0]) < 1.0e8 :
            im[row,column,:] = vec3(1, 0, 0)
        else:
            im[row,column,:] = background_color(ray_direction)

im = im * im
plt.imshow(im)
plt.show()
