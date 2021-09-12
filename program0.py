import numpy as np
import matplotlib.pyplot as plt
import math
import random

width = 512
height = 384

im = np.random.random(size=(height, width, 3))
im = im * im # approximate gamma correction, imshow expects non-linear intensites

plt.imshow(im)
plt.show()