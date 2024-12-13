import matplotlib.pyplot as plt

# Function to read timing data
def read_timing_data(filename):
    dp_n_values, dp_times = [], []
    exhaustive_n_values, exhaustive_times = [], []

    with open(filename, 'r') as f:
        for line in f:
            if line.startswith("DP"):
                parts = line.strip().split(": ")
                dp_n_values.append(int(parts[0].split()[1].split('x')[0]))
                dp_times.append(float(parts[1].split()[0]))
            elif line.startswith("Exhaustive"):
                parts = line.strip().split(": ")
                exhaustive_n_values.append(int(parts[0].split()[1].split('x')[0]))
                exhaustive_times.append(float(parts[1].split()[0]))

    return dp_n_values, dp_times, exhaustive_n_values, exhaustive_times

# Function to plot timing data
def plot_timing_data(dp_n_values, dp_times, exhaustive_n_values, exhaustive_times):
    # Plot DP timings
    plt.figure(figsize=(10, 5))
    plt.plot(dp_n_values, dp_times, 'o-r', label='Dynamic Programming')
    plt.xticks(dp_n_values)  # Ensure correct x-axis ticks for DP
    plt.yticks([round(t, 2) for t in dp_times])  # Ensure correct y-axis ticks for DP
    plt.xlabel('Grid Size (n x n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('DP Execution Time vs Grid Size', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot Exhaustive Search timings
    plt.figure(figsize=(10, 5))
    plt.plot(exhaustive_n_values, exhaustive_times, 'o-b', label='Exhaustive Search')
    plt.xticks(exhaustive_n_values)  # Ensure correct x-axis ticks for Exhaustive
    plt.yticks([round(t, 2) for t in exhaustive_times])  # Ensure correct y-axis ticks for Exhaustive
    plt.xlabel('Grid Size (n x n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Exhaustive Search Execution Time vs Grid Size', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage (assuming timing_results.txt exists):
if __name__ == "__main__":
    dp_n_values, dp_times, exhaustive_n_values, exhaustive_times = read_timing_data('timing_results.txt')
    plot_timing_data(dp_n_values, dp_times, exhaustive_n_values, exhaustive_times)
