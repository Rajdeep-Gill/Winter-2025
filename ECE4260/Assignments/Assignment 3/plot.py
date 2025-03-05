import matplotlib.pyplot as plt
import numpy as np

# Triangle Function
def triangle(t):
  if t < -1:
    return 0
  elif t < 0:
    return t + 1
  elif t < 1:
    return 1 - t
  else:
    return 0

# Signal
t = np.linspace(-50, 50, 10000)
x1 = np.array([triangle(i) for i in t])

fc = 8
b = 4
# f-3fc/b
# f- fc/b
# f+fc/b
# f+3fc/b
x1 = np.array([triangle((i-3*fc)/b) for i in t])
x2 = np.array([triangle((i-fc)/b) for i in t])
x3 = np.array([triangle((i+fc)/b) for i in t])
x4 = np.array([triangle((i+3*fc)/b) for i in t])

x_f = x1 + 3*x2 + 3*x3 + x4
x_f = x_f / 8

# Low-pass filter, ranges from -fc-B to fc + B
# 1 between, 0 outside
low_pass = np.array([1 if i >= -fc - b and i <= fc + b else 0 for i in t])


plt.figure(figsize = (8, 6))

plt.plot(t, x_f, label='X(f)')
# Vertical lines with labels
# Find y values at intersection points linestyle='--', label='fc')
fc_index = np.abs(t - fc).argmin()
neg_fc_index = np.abs(t - (-fc)).argmin()
three_fc_index = np.abs(t - 3*fc).argmin()
neg_three_fc_index = np.abs(t - (-3*fc)).argmin()
# Add x-axis labels
# Vertical lines with labels, stopping at signal-fc, 0, fc, 3*fc], ['-3fc', '-fc', '0', 'fc', '3fc'])
plt.vlines(x=fc, ymin=0, ymax=x_f[fc_index], color='r', linestyle='--')
plt.vlines(x=-fc, ymin=0, ymax=x_f[neg_fc_index], color='r', linestyle='--')
plt.xlabel('Frequency')
plt.vlines(x=3*fc, ymin=0, ymax=x_f[three_fc_index], color='r', linestyle='--')
plt.vlines(x=-3*fc, ymin=0, ymax=x_f[neg_three_fc_index], color='r', linestyle='--')

# Add x-axis labels with bandwidth points
xtick_positions = [-3*fc-b, -3*fc, -3*fc+b,    # -3fc points
                   -fc-b, -fc, -fc+b,           # -fc points
                   0,                           # center
                   fc-b, fc, fc+b,              # fc points
                   3*fc-b, 3*fc, 3*fc+b]       # 3fc points

xtick_labels = ['-3fc-B', '-3fc', '-3fc+B',
                '-fc-B', '-fc', '-fc+B',
                '0',
                'fc-B', 'fc', 'fc+B',
                '3fc-B', '3fc', '3fc+B']

plt.xticks(xtick_positions, xtick_labels, rotation=45)
plt.xlim(-3*fc-b - 5, 3*fc+b + 5)
plt.ylim(0, 0.4)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

# Enhanced grid settings
plt.grid(True, which='major', linestyle='-', alpha=0.5)
plt.grid(True, which='minor', linestyle=':', alpha=0.3)
plt.minorticks_on()
plt.title('X(f)')
plt.legend()
plt.tight_layout()
plt.savefig(
    "/Users/rajdeep/Documents/Winter 2025/ECE4260/Assignments/Assignment 3/images/p3_1.png")
plt.show()

plt.close()

plt.figure(figsize = (8, 8))
plt.subplot(2, 1, 1)
plt.plot(t, low_pass, label='Low Pass Filter')
plt.xlabel('Frequency')
plt.xticks([-fc-b, fc+b], ['-fc-B', 'fc+B'])
plt.ylabel('Amplitude')
plt.title('Low Pass Filter')
plt.grid(True, which="major", linestyle="-", alpha=0.5)
plt.grid(True, which="minor", linestyle=":", alpha=0.3)

plt.legend()
plt.tight_layout()

plt.subplot(2, 1, 2)
# Overlay the signal and the low pass filter

plt.plot(t, low_pass, label='Low Pass Filter')
plt.plot(t, x_f, label="X(f)")
# Vertical lines with labels
# Find y values at intersection points linestyle='--', label='fc')
fc_index = np.abs(t - fc).argmin()
neg_fc_index = np.abs(t - (-fc)).argmin()
three_fc_index = np.abs(t - 3 * fc).argmin()
neg_three_fc_index = np.abs(t - (-3 * fc)).argmin()
# Add x-axis labels
# Vertical lines with labels, stopping at signal-fc, 0, fc, 3*fc], ['-3fc', '-fc', '0', 'fc', '3fc'])
plt.vlines(x=fc, ymin=0, ymax=x_f[fc_index], color="r", linestyle="--")
plt.vlines(x=-fc, ymin=0, ymax=x_f[neg_fc_index], color="r", linestyle="--")
plt.xlabel("Frequency")
plt.vlines(x=3 * fc, ymin=0, ymax=x_f[three_fc_index], color="r", linestyle="--")
plt.vlines(x=-3 * fc, ymin=0, ymax=x_f[neg_three_fc_index], color="r", linestyle="--")

# Add x-axis labels with bandwidth points
xtick_positions = [
    -3 * fc - b,
    -3 * fc,
    -3 * fc + b,  # -3fc points
    -fc - b,
    -fc,
    -fc + b,  # -fc points
    0,  # center
    fc - b,
    fc,
    fc + b,  # fc points
    3 * fc - b,
    3 * fc,
    3 * fc + b,
]  # 3fc points

xtick_labels = [
    "-3fc-B",
    "-3fc",
    "-3fc+B",
    "-fc-B",
    "-fc",
    "-fc+B",
    "0",
    "fc-B",
    "fc",
    "fc+B",
    "3fc-B",
    "3fc",
    "3fc+B",
]

plt.xticks(xtick_positions, xtick_labels, rotation=45)
plt.xlim(-3 * fc - b - 5, 3 * fc + b + 5)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")

# Enhanced grid settings
plt.grid(True, which="major", linestyle="-", alpha=0.5)
plt.grid(True, which="minor", linestyle=":", alpha=0.3)
plt.minorticks_on()
plt.title("Low Pass Filter and X(f)")
plt.legend()
plt.tight_layout()
plt.savefig(
    "/Users/rajdeep/Documents/Winter 2025/ECE4260/Assignments/Assignment 3/images/p3_2.png"
)
plt.show()
plt.close()
