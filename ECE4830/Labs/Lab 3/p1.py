import matplotlib.pyplot as plt
import numpy as np
# Function 1:

def f1(x):
  # 1/16 sinc(pi/16 x)
  return np.sinc(x/16)

# Function 2:
def f2(x):
  # B cos(3pi/4 x)
  return np.cos(3*np.pi/4*x)

# fft of f1
y1 = np.fft.fft(f1(np.linspace(-30, 30, 1000)))

# fft of f2
y2 = np.fft.fft(f2(np.linspace(-30, 30, 1000)))

# Plotting
plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1)
plt.plot(np.linspace(-30, 30, 1000), f1(np.linspace(-30, 30, 1000)))
plt.title('f1(x)')
plt.xlabel('x')
plt.ylabel('f1(x)')

plt.subplot(2, 2, 2)
plt.plot(np.linspace(-30, 30, 1000), np.abs(y1))
plt.title('FFT of f1(x)')
plt.xlabel('k')
plt.ylabel('|F1(k)|')

plt.subplot(2, 2, 3)
plt.plot(np.linspace(-30, 30, 1000), f2(np.linspace(-30, 30, 1000)))
plt.title('f2(x)')
plt.xlabel('x')
plt.ylabel('f2(x)')

plt.subplot(2, 2, 4)
plt.plot(np.linspace(-30, 30, 1000), np.abs(y2))
plt.title('FFT of f2(x)')
plt.xlabel('k')
plt.ylabel('|F2(k)|')

plt.tight_layout()
plt.show()