# g(t) = piecewise:
# 0 from 0 to 6
# straight line starting at (6, -1) to (15, 0.5)
# straight line starting at (15, 0.5) to (24, 0)

# plot out g(3t)
# g(t+6)
# g(6-t)

import numpy as np
import matplotlib.pyplot as plt


def g(t):
    if t > 6 and t <= 15:
        return 1/6 * t - 2
    elif t > 15 and t <= 24:
        return -1/18 * t + 4/3
    else:
        return 0
    
plt.figure(1)
t = np.linspace(-30, 30, 1000)
plt.plot(t, [g(i) for i in t], 'r')
plt.xlim(0, 24)
plt.ylim(-1, 1)
plt.title('g(t)')
plt.xlabel('t')
plt.grid()
plt.savefig('ECE4260/Assignments/Assignment 1/images/p1_1.png')
plt.show()

plt.figure(2)
plt.plot(t, [g(3*i) for i in t], 'g')
plt.xlim(-24, 24)
plt.ylim(-1, 1)
plt.title('g(3t)')
plt.xlabel('t')
plt.grid()
plt.savefig('ECE4260/Assignments/Assignment 1/images/p1_2.png')
plt.show()

plt.figure(3)
plt.plot(t, [g(i+6) for i in t], 'b')
plt.xlim(-24, 24)
plt.ylim(-1, 1)
plt.title('g(t+6)')
plt.xlabel('t')
plt.grid()
plt.savefig('ECE4260/Assignments/Assignment 1/images/p1_3.png')
plt.show()

plt.figure(4)
plt.plot(t, [g(6-i) for i in t], 'm')
plt.xlim(-24, 24)
plt.ylim(-1, 1)
plt.title('g(6-t)')
plt.xlabel('t')
plt.grid()
plt.savefig('ECE4260/Assignments/Assignment 1/images/p1_4.png')
plt.show()

# plt.figure(5)
# plt.plot(t, [g(i) for i in t], label='g(t)')
# plt.plot(t, [g(3*i) for i in t], label='g(3t)')
# plt.plot(t, [g(i+6) for i in t], label='g(t+6)')
# plt.plot(t, [g(6-i) for i in t], label='g(6-t)')
# plt.legend()
# plt.xlim(-24, 24)
# plt.ylim(-1, 1)
# plt.title('All plots')
# plt.xlabel('t')
# plt.ylabel('g(t)')
# plt.grid()
# plt.show()

