
import matplotlib.pyplot as plt
import numpy as np

def unit_step(n):
    return 1 if n >= 0 else 0

# plot 1
# u[n-2] - u[n-6]

n = np.arange(-10, 10)
y1 = np.zeros(20)
for i in range(20):
    y1[i] = unit_step(n[i] - 2) - unit_step(n[i] - 6)

plt.figure(1)
plt.stem(n, y1)
plt.title('u[n-2] - u[n-6]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.ylim(-1, 7)
plt.grid(True)
plt.savefig('/Users/rajdeep/Documents/Winter 2025/ECE4830/Labs/Lab 1/images/plot1.png')

# plot 2
# n[u[n] - u[n-7]]
y2 = np.zeros(20)
for i in range(20):
    y2[i] = n[i] * (unit_step(n[i]) - unit_step(n[i] - 7))

plt.figure(2)
plt.stem(n, y2)
plt.title('n[u[n] - u[n-7]]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.ylim(-1, 7)

plt.grid(True)
plt.savefig('/Users/rajdeep/Documents/Winter 2025/ECE4830/Labs/Lab 1/images/plot2.png')

# plot 3
# (n-2)[u[n-2] - u[n-6]]
y3 = np.zeros(20)
for i in range(20):
    y3[i] = (n[i] - 2) * (unit_step(n[i]-2) - unit_step(n[i] - 6))

plt.figure(3)
plt.stem(n, y3)
plt.title('(n-2)[u[n-2] - u[n-6]]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.ylim(-1, 7)

plt.grid(True)
plt.savefig('/Users/rajdeep/Documents/Winter 2025/ECE4830/Labs/Lab 1/images/plot3.png')

# plot 4
# (-n+8)(u[n-6]-u[n-9])
y4 = np.zeros(20)
for i in range(20):
    y4[i] = (-n[i] + 8) * (unit_step(n[i] - 6) - unit_step(n[i] - 9))
    
plt.figure(4)
plt.stem(n, y4)
plt.title('(-n+8)(u[n-6]-u[n-9])')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.ylim(-1, 7)
plt.grid(True)
plt.savefig('/Users/rajdeep/Documents/Winter 2025/ECE4830/Labs/Lab 1/images/plot4.png')

# plot 5
# (n-2)[u[n-2] - u[n-6]] + (-n+8)(u[n-6]-u[n-9])
y5 = y3 + y4

plt.figure(5)
plt.stem(n, y5)
plt.title('(n-2)[u[n-2] - u[n-6]] + (-n+8)(u[n-6]-u[n-9])')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.ylim(-1, 7)

plt.grid(True)
plt.savefig('/Users/rajdeep/Documents/Winter 2025/ECE4830/Labs/Lab 1/images/plot5.png')
