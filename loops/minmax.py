#hackerranker
#2d array min max

import numpy as np

# Read input dimensions
n, m = map(int, input().split())

# Read the array
arr = np.array([input().split() for _ in range(n)], dtype=int)

# Find row-wise minimums
row_min = np.min(arr, axis=1)

# Find the maximum of those minimums
result = np.max(row_min)

# Print the result
print(result)
