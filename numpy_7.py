import numpy as np

# We create two rank 1 ndarrays
x = np.array([1, 2, 3, 4])
print('x = ', x)

y = np.array([5.5, 6.5, 7.5, 8.5])
print('y = ', y)

# We perform basic element-wise operations using arithmetic symbols and functions
print('x + y = ', x + y)
print('add(x,y) = ', np.add(x, y))
print()
print('x - y = ', x - y)
print('subtract(x,y) = ', np.subtract(x, y))
print()
print('x * y = ', x * y)
print('multiply(x,y) = ', np.multiply(x, y))
print()
print('x / y = ', x / y)
print('divide(x,y) = ', np.divide(x, y))

# --------------------------------------------------------------- #

# We create two rank 2 ndarrays
X = np.array([1, 2, 3, 4]).reshape(2, 2)
print('X = \n', X)
Y = np.array([5.5, 6.5, 7.5, 8.5]).reshape(2, 2)
print('Y = \n', Y)

print('X + Y = \n', X + Y)
print('X + Y = \n', np.add(X, Y))

print('X square root: \n', np.sqrt(X))
print('X exponential: \n', np.exp(X))
print('X raised to the power of 2: \n', np.power(X, 2))

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))
print()
print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X, axis=0))
print('Median of all elements in the rows of X:', np.median(X, axis=1))
print()
print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))
print()
print('Minimum value of all elements in X:', X.min())
print('Minimum value of all elements in the columns of X:', X.min(axis=0))
print('Minimum value of all elements in the rows of X:', X.min(axis=1))

# --------------------------------------------------------------- #

# We create a rank 1 ndarray
x = np.array([1, 2, 3])
print('x = ', x)

# We create a 3 x 3 ndarray
Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Y = \n', Y)

# We create a 3 x 1 ndarray
Z = np.array([1, 2, 3]).reshape(3, 1)
print('Z = \n', Z)

# Broadcasting (More info at https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)
print('x + Y = \n', x + Y)
print('Z + Y = \n', Z + Y)


# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc..

X = np.ones((4, 4), dtype=int) * np.arange(1, 5)
print('X = \n', X)
