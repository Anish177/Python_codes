import numpy as np
import matplotlib.pyplot as plt

# Set the number of items and the number of selections
n = 1000
k = 500

# Generate a large number of combinations and calculate the number of items selected for each combination
num_combinations = 1000000
selections = np.random.choice(range(n), size=(num_combinations, k), replace=True)
num_items_selected = np.sum(selections, axis=1)

# Plot the histogram of the number of items selected
plt.hist(num_items_selected, bins=20, density=True, alpha=0.5, color='b')

# Calculate the mean and standard deviation of the number of items selected
mean = np.mean(num_items_selected)
std = np.std(num_items_selected)

# Generate the x-values for the normal curve
x = np.linspace(mean - 3*std, mean + 3*std, 100)
# Calculate the y-values for the normal curve using the mean and standard deviation
y = 1/(std * np.sqrt(2 * np.pi)) * np.exp(-(x - mean)**2 / (2 * std**2))
# Plot the normal curve
plt.plot(x, y, color='r')

# Set the plot labels and title
plt.xlabel('Number of Items Selected')
plt.ylabel('Density')
plt.title('Approximation of Combinations Distribution')

# Display the plot
plt.show()
