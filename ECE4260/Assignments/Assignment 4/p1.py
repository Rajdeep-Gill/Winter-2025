import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn  # Bessel function of the first kind

# Carrier frequency (in Hz)
f_c = 10e5 # Example: 10 MHz

# Frequency deviations (multiples of 300 kHz)
delta_f = 300e3
n_values = np.arange(-3, 4)

# Create frequencies for both positive and negative carrier components
frequencies_pos = np.array([f_c + n * delta_f for n in n_values])
frequencies_neg = np.array([-f_c + n * delta_f for n in n_values])
frequencies = np.concatenate([frequencies_neg, frequencies_pos])

# Bessel coefficients (same for both positive and negative frequencies)
bessel_coeffs = np.array([jn(n, 2) for n in n_values])
bessel_coeffs_full = np.concatenate([bessel_coeffs, bessel_coeffs])

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.stem(frequencies/1e6, np.abs(bessel_coeffs_full), basefmt="k")

# Labels for significant components
for i, (f, Jn) in enumerate(zip(frequencies, bessel_coeffs_full)):
    if np.abs(Jn) > 0.01:
        n_idx = n_values[i % len(n_values)]
        ax.text(f/1e6, np.abs(Jn) + 0.02, f"$J_{{{n_idx}}}(2)$", ha="center", fontsize=10)

# Formatting
ax.set_xlabel("Frequency")
ax.set_ylabel("Magnitude")
ax.set_title("Magnitude of X_{FM}(f)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)

# Create symbolic x-axis labels
xticks = frequencies/1e6
symbolic_labels = []
for f in frequencies:
    if f < 0:
        base = "-f_c"
        offset = (f + f_c)/1e3
    else:
        base = "f_c"
        offset = (f - f_c)/1e3
    
    if offset == 0:
        symbolic_labels.append(f"${base}$")
    else:
        sign = "+" if offset > 0 else "-"
        symbolic_labels.append(f"${base}{sign}{abs(offset):.0f}$ kHz")

ax.set_xticks(xticks)
ax.set_xticklabels(symbolic_labels, rotation=45)

plt.ylim(0, 0.75)

plt.tight_layout()
plt.savefig("X_FM.png")
plt.show()
