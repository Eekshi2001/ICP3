import numpy as np

# Create a random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_array = random_vector.reshape(4, 5)

# Display the original array
print("Original Array:")
print(reshaped_array)
print("\n")

# Replace the max in each row by 0 (along axis=1)
reshaped_array[np.arange(reshaped_array.shape[0]), np.argmax(reshaped_array, axis=1)] = 0

# Display the modified array
print("Modified Array (Max in each row replaced by 0):")
print(reshaped_array)
