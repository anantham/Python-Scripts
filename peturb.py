import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# returns a random d dimensional vector, a direction to peturb in 
def direction(d,t):
    # if type == uniform
    if(t == 'u'):
        return np.random.uniform(-1/np.sqrt(2), 1/np.sqrt(2), d)
    elif(t == 'n'):
        return np.random.normal(0, 1/np.sqrt(d), d)
    elif(t == 's'):
        # a point on the N-Sphere
        angles = np.random.uniform(0, np.pi, d-2)
        x = np.zeros(d)
        x[0] = np.cos(angles[0])
        for i in range(1,d-1):
            temp = 1
            for j in range(i):
                temp = temp * np.sin(angles[j])
            x[i] = temp*np.cos(angles[i])
        x[d-1] = x[d-2]*np.tan(angles[d-2])
        return x

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(1000):
    R = np.random.uniform(0,1,1)[0]
    R2 = np.random.uniform(0,1,1)[0]
    xs = np.sin(np.arccos(1-2*R))*np.cos(2*np.pi*R2)
    ys = np.sin(np.arccos(1-2*R))*np.sin(2*np.pi*R2)
    zs = 1- 2*R
    ax.scatter3D(xs, ys, zs, cmap='Greens')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()