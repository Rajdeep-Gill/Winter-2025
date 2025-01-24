import numpy as np

# Define the unit step function
def unit_step(n):
    return 1 if n >= 0 else 0

# Initialize y[n] and x[n]
y = {}
x = {}

# Set initial conditions
y[-1] = 3
y[-2] = -1

# Compute y[n] for n from 0 to 9
for n in range(10):
    x[n] = unit_step(n)
    x[n-2] = unit_step(n-2)
    
    # Difference equation
    y[n] = (-1/6) * y[n-1] + (1/6) * y[n-2] + (1/3) * x[n] + (2/3) * x[n-2]

# Output the results
for n in range(10):
    print(f"y[{n}] = {y[n]}")
