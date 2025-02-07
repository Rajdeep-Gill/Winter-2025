import numpy as np
import matplotlib.pyplot as plt

def x_t(t, tau):
    """ Define x(t) = t^2 in the interval [-tau/2, tau/2] and 0 elsewhere."""
    return np.where(np.abs(t) <= tau / 2, t**2, 0)

def g_t(t, tau, T):
    """ Define g(t) as the periodic summation of x(t). """
    g_t_values = np.zeros_like(t)
    for k in range(-5, 6):  # Sum over multiple periods for better visualization
        g_t_values += x_t(t - k * T, tau)
    return g_t_values

# Define parameters
tau = 2  # Width of x(t)
T = 4     # Period of g(t), must be >= tau

# Time range for plotting
t_vals = np.linspace(-2*T - tau/2, 2*T + tau/2, 1000)

# Compute x(t) and g(t)
x_vals = x_t(t_vals, tau)
g_vals = g_t(t_vals, tau, T)

# Plot x(t)
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t_vals, x_vals, 'b', label='$x(t) = t^2$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title('Original Signal $x(t)$')

# Plot g(t)
plt.subplot(2, 1, 2)
plt.plot(t_vals, g_vals, 'r', label='$g(t)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title('Periodic Signal $g(t)$')

plt.tight_layout()
plt.savefig('ECE4260/Assignments/Assignment 2/images/p5.png')
plt.show()
