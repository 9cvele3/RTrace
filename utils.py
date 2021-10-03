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
