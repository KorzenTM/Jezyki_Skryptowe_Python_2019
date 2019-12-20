# -*- coding: utf-8 -*-
#diagonal projection

import math
import numpy as np
import matplotlib.pyplot as plt

g=9.81

def max_height(v0,angle):
    h_max=(v0**2*np.sin(angle)**2)/(2*g)
    return h_max
def reach(v0,angle):
    Z=(v0**2/g)*np.sin(2*angle)
    return Z
def time(v0,angle):
    T=(2*v0*np.sin(angle))/g
    return T


v0=float(input("Initial speed:"))
angle=math.radians(float(input("Angle:")))
height=max_height(v0,angle)
reach=reach(v0,angle)
time=time(v0,angle)
print("Max height:",height)
print("Reach:",reach)
print("Time:",time)

t=np.arange(0,time,0.1)
plt.subplot(3,1,1)
plt.plot(t,v0*np.sin(angle)-g*t)
plt.hlines(y=v0*np.cos(angle),xmin=0,xmax=time)
plt.grid(True)
plt.xlabel("Time - t[s]")
plt.ylabel("Velocity = v[m/s]")
plt.subplot(3,1,2)
v0x=v0*np.cos(angle)
v0y=v0*np.sin(angle)-g*t
v=np.sqrt(v0x**2+v0y**2)
plt.plot(t,v)
plt.xlabel("t[s]")
plt.ylabel("v[m/s]")
plt.grid(True)
plt.subplot(3,1,3)
x=np.arange(0,reach,0.1)
plt.plot(x,x*np.tan(angle)-((g)/(2*v0**2*np.cos(angle)**2))*x**2)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y=f(x)")
plt.show()
