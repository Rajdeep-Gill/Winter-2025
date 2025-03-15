import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('output.txt', skiprows=1, delimiter=',')
x = data[:, 0]
y = data[:, 1]

plt.figure()
plt.title("Throughput vs Probability of Loss")
plt.scatter(x, y)
plt.xlabel("Probability of Loss")
plt.ylabel("Throughput")
plt.plot(x, y)
plt.grid(True, which="major", linestyle="-", alpha=0.5)
plt.grid(True, which="minor", linestyle=":", alpha=0.3)
plt.xticks(x)
plt.minorticks_on()
plt.savefig("throughput vs probability of loss.png")
plt.show()

data_ploss_80 = np.loadtxt('output_ploss0.8.txt', skiprows=1, delimiter=',')
data_ploss_90 = np.loadtxt('output_ploss0.9.txt', skiprows=1, delimiter=',')

x_80 = data_ploss_80[:, 0]
y_80 = data_ploss_80[:, 1]

x_90 = data_ploss_90[:, 0]
y_90 = data_ploss_90[:, 1]

plt.figure()
plt.title("Throughput vs Window size")
plt.scatter(x_80, y_80, label="ploss = 0.8")
plt.scatter(x_90, y_90, label="ploss = 0.9")
plt.xlabel("Window Size")
plt.ylabel("Throughput")
plt.plot(x_80, y_80)
plt.plot(x_90, y_90)
plt.legend()
plt.grid(True, which="major", linestyle="-", alpha=0.5)
plt.grid(True, which="minor", linestyle=":", alpha=0.3)
plt.xticks(x_80)
plt.minorticks_on()
plt.savefig("throughput vs window size.png")
plt.show()
