import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np

R = 60 #float(raw_input(" R = "))
r = 10 #float(raw_input(" r = "))
reps = 3 #int(raw_input("Number of repetitions = "))

circumference = reps * 360
x_points = []
y_points = []
x_2_points = []
y_2_points = []

print ("Epicycloid and Epitrochoid")
for s in range(0,circumference):
    x = (R + r) * cos(radians(s)) - r * cos(radians(((R + r)/r)*s))
    y = (R + r) * sin(radians(s)) - r * sin(radians(((R + r)/r)*s))
    x_points.append(x)
    y_points.append(y)
    x_2 = (R + r) * cos(radians(s)) - 30 * cos(radians(((R + r) / r) * s))
    y_2 = (R + r) * sin(radians(s)) - 30 * sin(radians(((R + r) / r) * s))
    x_2_points.append(x_2)
    y_2_points.append(y_2)

raza = plt.Line2D((0, 0), (0, 0), linewidth=1, color="k")
circler = plt.Circle((0, 0), r, color='r', fill=False)
circleR = plt.Circle((0, 0), R, color='r', fill=False)
punct = plt.Circle((0, 0), float(float(r)/10), color="r")
fig, ax = plt.subplots()
ax.set_xlim(-2*(R + r),2*(R + r))
ax.set_ylim(-2*(R + r),2*(R + r))
trace, = ax.plot([], [], color="b")
trace2, = ax.plot([], [], color="k")
ax.add_artist(circleR)
ax.add_artist(raza)
ax.add_artist(punct)
ax.add_artist(circler)
ax.add_artist(trace)
ax.add_artist(trace2)


def init():
    circler.center = (0, 0)
    punct.center = (0, 0)
    ax.add_patch(circler)
    ax.add_patch(punct)
    return circler, punct,


def animate(i):
    x = (r +  R) * np.cos(np.radians(i))
    y = (r + R) * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    # x_2 = x_2_points[i]
    # y_2 = y_2_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.center = (x2, y2)
    trace.set_data((x_points[:i], y_points[:i]))
    trace2.set_data((x_2_points[:i], y_2_points[:i]))
    return circler, punct, raza, trace, trace2


anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)

plt.grid()
plt.show()