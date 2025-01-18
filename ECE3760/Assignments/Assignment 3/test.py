import numpy as np

# Guess distribution data
guesses = [2, 3, 4, 5, 6]  # The number of guesses
frequencies = [17, 191, 172, 58, 16]  # The corresponding frequencies

# Total games played
total_games = sum(frequencies)

# Calculate the mean
mean = sum(g * f for g, f in zip(guesses, frequencies)) / total_games

# Calculate the variance
variance = sum(g**2 * f for g, f in zip(guesses, frequencies)) / total_games - mean**2

# Calculate the standard deviation
std_dev = np.sqrt(variance)

variance_mean = variance / total_games

# Calculate the standard error of the mean
sem = std_dev / np.sqrt(total_games)

# Print the results
print(f"Mean: {mean:.3f}")
print(f"Variance: {variance:.3f}")
print(f"Standard Deviation: {std_dev:.3f}")
print(f"Variance of the Mean: {variance_mean:.3f}")
print(f"Standard Error of the Mean: {sem:.3f}")
