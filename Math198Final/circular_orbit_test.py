from scipy.integrate import odeint
import math
import numpy as np
import matplotlib.pyplot as plt


U_x = []
U_y = []


def dU_dx(U, x):
    U_x.append(U[0])
    U_y.append(U[1])

    x_prime = -U[1]
    y_prime = U[0]

    return [x_prime, y_prime]


duration = 10
resolution = 100

U0 = [1, 0]
xs = np.linspace(0, duration, resolution)
Us = odeint(dU_dx, U0, xs)
ys = Us[:, 0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

ax1.set_title('circular orbit test')
ax1.plot(xs, ys)
ax1.set_xlabel('t')
ax1.set_ylabel('x')

ax2.set_title('trajectory')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.plot(U_x, U_y)

plt.show()
