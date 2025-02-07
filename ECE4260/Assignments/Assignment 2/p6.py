import matplotlib.pyplot as plt
import numpy as np

def g(t):
  return np.where((0 <= t) & (t <= 1), 1-t, 0)

t = np.linspace(-2, 5, 1000)
g1 = g(t)

plt.figure()
plt.plot(t, g1)
plt.xlim(-1, 2)
plt.ylim(-1, 2)
plt.show()

g_even = 0.5 * (g(t) + g(-t))
g_odd = 0.5 * (g(t) - g(-t))

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, g_even)
plt.title("Even part")
plt.xlim(-2, 2)
plt.ylim(-1, 1)

plt.subplot(2, 1, 2)
plt.plot(t, g_odd, label='Odd part')
plt.title("Odd part")
plt.xlim(-2, 2)
plt.ylim(-1, 1)

plt.tight_layout()
plt.savefig('ECE4260/Assignments/Assignment 2/images/p6.png')
plt.show()