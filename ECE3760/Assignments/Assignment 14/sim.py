import numpy as np

p = 0.01 # Probability / lambda
num_iterations = 10000


def simulate_simplex(p):
    time_steps = 0
    while True:
        time_steps += 1
        if np.random.rand() < p:
            break
    return time_steps


def simulate_tmr(p):
    time_steps = 0
    working_modules = 3
    while working_modules >= 2:
        time_steps += 1
        failures = np.random.rand(working_modules) < p
        working_modules -= np.sum(failures)
    return time_steps


def simulate_redundant_to_simplex(p):
    time_steps = 0
    active_modules = 3
    switched_to_simplex = False

    while True:
        time_steps += 1
        failures = np.random.rand(active_modules) < p
        active_modules -= np.sum(failures)

        if not switched_to_simplex and active_modules < 3:
            active_modules = 1  # Switch to simplex
            switched_to_simplex = True

        if active_modules <= 0:
            break

    return time_steps


# Run simulations
simplex_times = [simulate_simplex(p) for _ in range(num_iterations)]
tmr_times = [simulate_tmr(p) for _ in range(num_iterations)]
redundant_to_simplex_times = [
    simulate_redundant_to_simplex(p) for _ in range(num_iterations)
]

avg_simplex = np.mean(simplex_times)
avg_tmr = np.mean(tmr_times)
avg_redundant_to_simplex = np.mean(redundant_to_simplex_times)

print(f"Average time to failure (Simplex): {avg_simplex:.2f} steps")
print(f"Average time to failure (TMR): {avg_tmr:.2f} steps")
print(
    f"Average time to failure (TMR-to-Simplex): {avg_redundant_to_simplex:.2f} steps"
)
