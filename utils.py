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
