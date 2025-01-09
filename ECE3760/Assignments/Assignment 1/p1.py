import numpy as np
SIZE_SAMPLES = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

for size in SIZE_SAMPLES:
  samples = np.random.randint(1, 26, (size, 2))
  max_sample = np.max(samples, axis=1) # max of each sample

  # expected value of max_sample
  expected_value = np.mean(max_sample)
  print("Expected value: ", expected_value, "for size: ", size)

