import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from mpl_toolkits.mplot3d import Axes3D

m = 1024
b = 3
#a = range(0,1024)
x = 0

for a in range(0,1024):
    for x 






x, y, z = np.random.normal(size =(3 , 1000))



fig = plt.figure()
ax = fig.add_subplot(111 , projection ='3d')

ax.view_init(45 , 30) # Elevation , Rotation
ax.scatter(
    x, y, z,
    lw=0, # no lines around points
    s=5, # smaller points
)
plt.show()
