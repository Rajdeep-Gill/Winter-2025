import matplotlib.pyplot as plt
def unit_step(n):
    return 1 if n >= 0 else 0

y = {}
x = {}

# Initial conditions
y[-1] = 3
y[-2] = -1

for n in range(10):
    x[n] = unit_step(n)
    x[n-2] = unit_step(n-2)
    y[n] = (-1/6) * y[n-1] + (1/6) * y[n-2] + (1/3) * x[n] + (2/3) * x[n-2]
    print(f"y[{n}] = {y[n]:.5f}")

plt.stem(y.keys(), y.values())
plt.title("Plot of y[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid()
plt.savefig('p3.png')
plt.show()