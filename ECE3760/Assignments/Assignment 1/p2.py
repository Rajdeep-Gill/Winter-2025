import numpy as np

nums_range = np.arange(1, 26)
num_trials = 1_000_000
samples_per_trial = 2 

samples = np.array([
    np.random.choice(nums_range, size=samples_per_trial, replace=False) for _ in range(num_trials)
])

max_numbers = np.max(samples, axis=1)
expected_value = np.mean(max_numbers)

print(expected_value)
