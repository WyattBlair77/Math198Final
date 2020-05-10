from scipy.integrate import odeint
import math
import numpy as np
import matplotlib.pyplot as plt

a = 0.75
b = 0.05
g = 0.04

e = 0.3


eps = 0.001

print('e > 0.619 : ', e > 0.619)

theta_vals = []


def dU_dx(U, x):
    theta_prime = eps*(2*e*(1+U[1])*math.sin(x) + e*a*math.cos(x)*math.sin(2*U[0]) - b*U[1] - g*U[1] * abs(U[1])) - a*math.sin(2*U[0])
    theta = eps*(-g*U[1]**2 + U[1]*(2*e*math.sin(x)-b) + 2*e*math.sin(x)*e*a*math.cos(x)*math.sin(2*U[0])) - a*math.sin(2*U[0] - theta_prime)
    theta_vals.append(theta)
    return [theta, theta_prime]


duration = 500

resolution = 1000

U0 = [0, 0]
xs = np.linspace(0, duration, resolution)
Us = odeint(dU_dx, U0, xs)
ys = Us[:, 0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

ax1.set_title('e value: ' + str(e))
ax1.plot(xs, ys)
ax1.set_xlabel('v')
ax1.set_ylabel('psi')

ax2.set_title('trajectory')
ax2.set_xlabel('psi')
ax2.set_ylabel('d/dv (psi)')
ax2.plot(ys[0:len(theta_vals)], theta_vals[0:len(ys)])

plt.show()
