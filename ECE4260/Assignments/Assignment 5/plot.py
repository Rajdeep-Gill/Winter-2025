import numpy as np
import matplotlib.pyplot as plt


# Define the sinc function using the sin(pi t) / (pi t) definition
def sinc(t):
    return np.sinc(t)  # np.sinc is normalized as sin(pi t)/(pi t)


# Time constant T
T = 1  # You can change this value if needed

# Δf range
delta_f = np.linspace(-2, 2, 1000)

# Compute the function values
y = sinc(2 * delta_f * T)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(delta_f, y, label=r"$\mathrm{sinc}(2 \Delta f T)$")
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
plt.axvline(0, color="gray", linestyle="--", linewidth=0.8)

# Label key x-axis points
xticks = [-1.5,-0.7, -1, -0.5, 0, 0.5, 1 ,0.7, 1.5]
xtick_labels = [
    r"$-\frac{3}{2T}$",
    r"$-\frac{1.4}{2T}$",
    r"$-\frac{1}{T}$",
    r"$-\frac{1}{2T}$",
    "0",
    r"$\frac{1}{2T}$",
    r"$\frac{1}{T}$",
    r"$\frac{1.4}{2T}$",
    r"$\frac{3}{2T}$",
]
yticks = [-0.216, 0, 0.5, 1, 1.5]
print(len(xtick_labels), len(xticks))
plt.xticks(xticks, xtick_labels)
plt.yticks(yticks)

plt.xlabel(r"$\Delta f$")
plt.ylabel(r"$\mathrm{sinc}(2 \Delta f T)$")
plt.title(r"$\mathrm{sinc}(2 \Delta f T)$")
plt.grid(True, which="minor", linestyle=":", alpha=0.3)
plt.grid(True, which="major", linestyle="-", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("sinc_plot.png")
plt.show()
