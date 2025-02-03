import numpy as np

dataset = np.random.randint(1, 51, size = (5, 5))
print("Original: \n", dataset)

dataset[dataset > 25] = 0
print("Modified: \n", dataset)

print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))