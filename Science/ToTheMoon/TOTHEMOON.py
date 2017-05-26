"""Import relevant packages."""
import numpy as np
# import math

# MOOOOOOON

# Constants
Re = 6378.14  # km
Rm = 1737.4  # km
LEO = 222  # km
a12 = 384400  # km
mu = 0.01215
omegam = 2.6491e-6  # rad/s
mu3 = 3.986e5  # km^3/s^2
nu = 0
e = 0
omega = (0, 0, omegam)
dv = a12*omegam

print(omega)

# Target Altitudes
Earth_target = (150, 200)
Moon_target = (200, 300)

# Set time step for test cases and free return orbit
t0 = 0
tf = .1
tspan = (t0, tf)

# Test case L4
# Initial Conditions
x = -1./2+mu
y = np.sqrt(3.)/2
vx = 0
vy = 0
x0 = (vx, vy, x, y)
print(x0)

# def threebody()
