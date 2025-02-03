import numpy as np
import matplotlib.pyplot as plt

def g(t):
  if t < 0 and t > -1:
    return -t
  
  return 0

t = np.linspace(-2, 2, 1000)
y0 = np.array([g(i) for i in t])
# \item $g_1(t) = g(-t)$
# \item $g_2(t) = g_1(t-1) + g(t-1) = g(-t+1) + g(t-1)$
# \item $g_3(t) = g_1(t+1) + g(t-1) = g(-t-1) + g(t-1)$
# \item $g_4(t) = g_1(t+1/2) + g(t-1/2) = g(-t-1/2) + g(t-1/2)$
# \item $g_5(t) = \frac{3}{2}g(\frac{t}{2}-1)$
y1 = np.array([g(-i) for i in t])
y2 = np.array([g(-i+1) + g(i-1) for i in t])
y3 = np.array([g(-i-1) + g(i-1) for i in t])
y4 = np.array([g(-i-1/2) + g(i-1/2) for i in t])
y5 = np.array([3/2*g(i/2-1) for i in t])

plt.plot(t, y0, label='g(t)')
plt.show()
plt.plot(t, y1, label='g_1(t)')
plt.show()
plt.plot(t, y2, label='g_2(t)')
plt.show()
plt.plot(t, y3, label='g_3(t)')
plt.show()
plt.plot(t, y4, label='g_4(t)')
plt.show()
plt.plot(t, y5, label='g_5(t)')
plt.show()
