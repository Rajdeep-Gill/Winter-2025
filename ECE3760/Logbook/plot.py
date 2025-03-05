import numpy as np
import matplotlib.pyplot as plt

# Sender
# \frac{500\cdot0.8}{65x+15\left(1-x\right)}\left\{0\le x\le1\right\}
x = np.linspace(0, 1, 100)
y1= 500*0.8/(65*x+15*(1-x))
# Receiver
# \frac{500\cdot0.8}{75x+35\left(1-x\right)}
y2 = 500*0.8/(75*x+35*(1-x))


plt.figure(figsize=(8,6))
plt.plot(x, y1, label='Sender')
plt.plot(x, y2, label='Receiver')
plt.xlabel('Active Percentage')
plt.ylabel('Battery Life (hours)')
plt.title('Battery Life vs Active Percentage')
plt.legend()
plt.grid(True, which="major", linestyle="-", alpha=0.5)
plt.grid(True, which="minor", linestyle=":", alpha=0.3)
plt.minorticks_on()
plt.savefig('battery_life.png')
plt.show()