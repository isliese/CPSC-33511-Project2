import matplotlib.pyplot as plt
import numpy as np

# Function to read timing data
def read_timing_data(filename):
    dp_n_values, dp_times = [], []
    exhaustive_n_values, exhaustive_times = [], []

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(": ")
            size = int(parts[0].split('x')[0])  # Extract grid size
            time = float(parts[1].split()[0])  # Extract time value
            
            # Determine if the line corresponds to DP or Exhaustive based on size
            if size >= 100:  # DP grid sizes are larger
                dp_n_values.append(size)
                dp_times.append(time)
            else:  # Exhaustive grid sizes are smaller
                exhaustive_n_values.append(size)
                exhaustive_times.append(time)

    return dp_n_values, dp_times, exhaustive_n_values, exhaustive_times

# Function to plot timing data with theoretical complexity
def plot_timing_data(dp_n_values, dp_times, exhaustive_n_values, exhaustive_times):
    # Theoretical complexity curves
    n_values_dp = np.array(dp_n_values)
    n_values_exhaustive = np.array(exhaustive_n_values)

    # Theoretical time complexity curves
    theoretical_dp = n_values_dp**2  # O(n^2) 
    theoretical_exhaustive = n_values_exhaustive * 2**n_values_exhaustive  # O(n * 2^n)

    # Normalize theoretical curves to match the scale of measured data
    theoretical_dp = theoretical_dp / max(theoretical_dp) * max(dp_times)
    theoretical_exhaustive = theoretical_exhaustive / max(theoretical_exhaustive) * max(exhaustive_times)

    # Plot DP timings
    plt.figure(figsize=(12, 6))
    plt.plot(dp_n_values, dp_times, 'o-r', label='Measured DP Times (O(n²))')
    plt.plot(n_values_dp, theoretical_dp, '--r', label='Theoretical O(n²)')

    plt.xlabel('Grid Size (n x n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('DP Execution Time vs Grid Size', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot Exhaustive Search timings
    plt.figure(figsize=(12, 6))
    plt.plot(exhaustive_n_values, exhaustive_times, 'o-b', label='Measured Exhaustive Times (O(n·2ⁿ))')
    plt.plot(n_values_exhaustive, theoretical_exhaustive, '--b', label='Theoretical O(n·2ⁿ)')

    plt.xlabel('Grid Size (n x n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Exhaustive Search Execution Time vs Grid Size', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filename = 'timing_results.txt'  # file name
    dp_n_values, dp_times, exhaustive_n_values, exhaustive_times = read_timing_data(filename)
    
    # Print data for debugging
    print("DP Sizes:", dp_n_values)
    print("DP Times:", dp_times)
    print("Exhaustive Sizes:", exhaustive_n_values)
    print("Exhaustive Times:", exhaustive_times)
    
    plot_timing_data(dp_n_values, dp_times, exhaustive_n_values, exhaustive_times)
