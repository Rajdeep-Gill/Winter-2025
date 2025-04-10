import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Parameters ---
# Estimate 1 (Odometry - from previous calculation)
mean1 = 100.0
variance1 = 4.0
std_dev1 = np.sqrt(variance1)

# Estimate 2 (GPS/External Sensor)
mean2 = 105.0
variance2 = 1.0
std_dev2 = np.sqrt(variance2)

# --- Calculate Fused Parameters ---
# Precision (Inverse Variance)
precision1 = 1 / variance1
precision2 = 1 / variance2
total_precision = precision1 + precision2

# Fused Variance
variance_fused = 1 / total_precision
std_dev_fused = np.sqrt(variance_fused)

# Fused Mean
mean_fused = variance_fused * (mean1 * precision1 + mean2 * precision2)

print("--- Input Estimates ---")
print(
    f"Estimate 1 (Odometry): Mean={mean1:.2f}, Variance={variance1:.2f}, StdDev={std_dev1:.2f}"
)
print(
    f"Estimate 2 (GPS):      Mean={mean2:.2f}, Variance={variance2:.2f}, StdDev={std_dev2:.2f}"
)
print("\n--- Fused Estimate ---")
print(
    f"Fused Estimate:        Mean={mean_fused:.2f}, Variance={variance_fused:.2f}, StdDev={std_dev_fused:.3f}"
)

# --- Generate Data for Plotting ---
# Determine a suitable range for the x-axis to show all distributions
plot_min = min(
    mean1 - 4 * std_dev1, mean2 - 4 * std_dev2, mean_fused - 4 * std_dev_fused
)
plot_max = max(
    mean1 + 4 * std_dev1, mean2 + 4 * std_dev2, mean_fused + 4 * std_dev_fused
) + 4
x = np.linspace(plot_min, plot_max, 500)

# Calculate the PDF values
pdf1 = norm.pdf(x, loc=mean1, scale=std_dev1)
pdf2 = norm.pdf(x, loc=mean2, scale=std_dev2)
pdf_fused = norm.pdf(x, loc=mean_fused, scale=std_dev_fused)

# --- Plotting ---
plt.figure(figsize=(10, 6))

plt.plot(
    x,
    pdf1,
    label=f"Odometry Estimate (μ={mean1:.1f}, σ={std_dev1:.1f})",
    linestyle="--",
)
plt.fill_between(x, pdf1, alpha=0.2)

plt.plot(
    x, pdf2, label=f"GPS Estimate (μ={mean2:.1f}, σ={std_dev2:.1f})", linestyle=":"
)
plt.fill_between(x, pdf2, alpha=0.2)

plt.plot(
    x,
    pdf_fused,
    label=f"Fused Estimate (μ={mean_fused:.1f}, σ={std_dev_fused:.2f})",
    color="red",
    linewidth=2,
)
plt.fill_between(x, pdf_fused, alpha=0.3, color="red")

plt.xlabel("Position (meters)")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("fused_estimate_plot.png")  # Save the figure
plt.show()