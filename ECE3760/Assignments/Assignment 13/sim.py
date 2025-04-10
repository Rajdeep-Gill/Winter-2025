import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Parameters ---
# Single Stride
mean1 = 1.0  # meters
std_dev1 = 0.2  # meters
variance1 = std_dev1**2  # meters^2

# 100 Strides
N = 100
mean100 = N * mean1
variance100 = N * variance1
std_dev100 = np.sqrt(variance100)  # Equivalent to std_dev1 * np.sqrt(N)

print(f"Parameters for 1 stride:")
print(f"  Mean: {mean1:.2f} m")
print(f"  Standard Deviation: {std_dev1:.2f} m")
print(f"  Variance: {variance1:.2f} m^2")
print("-" * 20)
print(f"Parameters for {N} strides:")
print(f"  Mean: {mean100:.2f} m")
print(f"  Standard Deviation: {std_dev100:.2f} m")
print(f"  Variance: {variance100:.2f} m^2")
print("-" * 20)

# --- Generate Data for Plotting ---
# Range for x-axis (position). Go out ~4 standard deviations from the mean
x1 = np.linspace(mean1 - 4 * std_dev1, mean1 + 4 * std_dev1, 500)
x100 = np.linspace(mean100 - 4 * std_dev100, mean100 + 4 * std_dev100, 500)

# Calculate the PDF values
pdf1 = norm.pdf(x1, loc=mean1, scale=std_dev1)
pdf100 = norm.pdf(x100, loc=mean100, scale=std_dev100)

# --- Plotting ---
fig, axs = plt.subplots(2, 1, figsize=(8, 8))  # Create 2 subplots vertically

# Plot for 1 Stride
axs[0].plot(x1, pdf1, label=f"μ={mean1:.1f}, σ={std_dev1:.1f}")
axs[0].set_title("PDF of Robot Position after 1 Stride")
axs[0].set_xlabel("Position (meters)")
axs[0].set_ylabel("Probability Density")
axs[0].fill_between(x1, pdf1, alpha=0.3)
axs[0].grid(True)
axs[0].legend()
# Add vertical lines for mean +/- std dev
axs[0].legend()


# Plot for 100 Strides
axs[1].plot(x100, pdf100, label=f"μ={mean100:.0f}, σ={std_dev100:.1f}")
axs[1].set_title(f"PDF of Robot Position after {N} Strides")
axs[1].set_xlabel("Position (meters)")
axs[1].set_ylabel("Probability Density")
axs[1].fill_between(x100, pdf100, alpha=0.3)
axs[1].grid(True)
axs[1].legend()
axs[1].legend()

# Adjust layout and display plot
plt.tight_layout()  # Prevents labels from overlapping
plt.savefig("pdf_plots.png")  # Save the figure
plt.show()
