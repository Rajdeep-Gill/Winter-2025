import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fc = 0  # Center frequency
w = 1 # Half-width of the triangle

# Define x (frequency) values
x = np.linspace(fc - w - 100, fc + w + 100, 40900)  # Slightly extended range for clarity

# Define triangular function
g_f = np.maximum(1 - np.abs(x - fc) / w, 0)  # Triangle function


# Define parameters
fc = 10  # Center frequency
w = 5  # Half-width of the triangle

# Define x (frequency) values
x = np.linspace(fc - w - 100, fc + w + 100, 40000)  # Extended range for clarity
x_shifted = x - fc  # Shifted x-axis for Y(f)

# Define triangular function
G_f = np.maximum(1 - np.abs(x - fc) / w, 0)  # Original triangle function
Y_f = np.maximum(1 - np.abs(x_shifted) / w, 0)  # Shifted triangle function


# Show plots
plt.tight_layout()
plt.show()

# Plot
plt.plot(x_shifted, Y_f, "b", label="$g(f)$")

# Labels and ticks
plt.xlabel("$f$")
plt.xticks([-w, 0, w], [r"$-w$", r"$0$", r"$w$"])  # Label -w, 0, w
plt.yticks([0, 1], ["0", r"$2G(f_c)$"])  # Label 1 as G(fc)

# Grid and formatting
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(fc - w, color="gray", linestyle="--", linewidth=0.5)
plt.axvline(fc + w, color="gray", linestyle="--", linewidth=0.5)
plt.axvline(fc, color="gray", linestyle="--", linewidth=0.5)

plt.xlim(-8, 8)
plt.ylim(-0.2, 2)

# Show plot
plt.grid(True, linestyle="--", linewidth=0.5)
plt.savefig("p2_2.png")
plt.show()
