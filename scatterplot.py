import matplotlib.pyplot as plt

# Read timing data from the file
def read_timing_data(filename='timing_results.txt'):
    n_values = []
    times = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(": ")
            n_values.append(int(parts[0].split('x')[0]))  # Extract n value
            times.append(float(parts[1].split()[0]))  # Extract time value
    return n_values, times

# Plotting the timing data
def plot_timing_data(n_values, times):
    # Scatter plot
    plt.scatter(n_values, times, color='blue', label='Data points')

    # Optionally, fit a line (linear or logarithmic based on the data pattern)
    plt.plot(n_values, times, 'r-', label='Best fit line')

    # Labels and title
    plt.xlabel('Grid Size (n x n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Execution Time vs Grid Size', fontsize=14)

    # Show plot
    plt.legend()
    plt.grid(True)
    plt.show()

# Load the data
n_values, times = read_timing_data()

# Plot the data
plot_timing_data(n_values, times)
