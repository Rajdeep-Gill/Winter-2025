import matplotlib.pyplot as plt
import numpy as np

#x1 = square pulse, ampltiude = 1, start at 0, end at 2

def x(t):
  return np.where((0 <= t) & (t <= 2), 1, 0)

#y1(t) = triangle pulse, amplitude = 2, start at 0, peak at (1, 2), end at 2
def y(t):
  # y = 2t, 0 <= t <= 1
  # y= 4 - 2t, 1 <= t <= 2
  # else 0

  return np.where((0 <= t) & (t <= 1), 2*t, np.where((1 < t) & (t <= 2), 4 - 2*t, 0))

t = np.linspace(-2, 5, 1000)

x1 = x(t)
y1 = y(t)
#x2 = x1 - x(t-2) = x(t) - x(t-2)
x2 = x(t) - x(t-2)
y2 = y(t) - y(t-2)
#x3 =  x(t+1) + 2x(t) + x(t-1)
x3 = x(t+1) + x(t)
y3 = y(t+1) + y(t)

plt.figure(figsize = (8, 8))
plt.subplot(3, 2, 1)
plt.plot(t, x1)
plt.title('x1(t)')
plt.grid()

plt.subplot(3, 2, 2)
plt.plot(t, y1)
plt.title('y1(t)')
# Show point (1, 2)
plt.plot(1, 2, 'ro')
plt.text(1, 2, '(1, 2)')
plt.ylim(-0.5, 2.5)
plt.grid()

plt.subplot(3, 2, 3)
plt.plot(t, x2)
plt.title('x2(t)')
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(t, y2)
# Show point (1, 2) and (3, -2)
plt.plot(1, 2, 'ro')
plt.plot(3, -2, 'ro')
plt.text(1, 2, '(1, 2)')
plt.text(3, -2, '(3, -2)')
plt.ylim(-2.5, 2.5)
plt.title('y2(t)')
plt.grid()

plt.subplot(3, 2, 5)
plt.plot(t, x3)
plt.title('x3(t)')
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(t, y3)
#show point (0, 2), (1, 2)
plt.plot(0, 2, 'ro')
plt.plot(1, 2, 'ro')
plt.text(0, 2, '(0, 2)')
plt.text(1, 2, '(1, 2)')
plt.ylim(-0.5, 2.5)
plt.title('y3(t)')
plt.grid()

plt.tight_layout()
plt.savefig("/Users/rajdeep/Documents/Winter 2025/ECE4260/Assignments/Assignment 2/images/plot.png")
plt.show()