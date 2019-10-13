import numpy as np

# We create a 5 x 5 ndarray that contains integers from 0 to 19
x = np.arange(25).reshape((5, 5))
print('x = \n', x)

# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', x[x > 10])
print('The elements in X that are between 10 and 17:', x[(x > 10) & (x < 17)])

# We use Boolean indexing to assign the elements that are between 10 and 17 the value of -1
x[(x > 10) & (x < 17)] = -1
print('x = \n', x)
print()

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We create a rank 1 ndarray
y = np.array([6, 7, 2, 8, 4])

# --------------------------------------------------------------- #

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])
print('x = ', x)

# We create a rank 1 ndarray
y = np.array([6, 7, 2, 8, 4])
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x, y))
print('The elements that are in x that are not in y:', np.setdiff1d(x, y))
print('All the elements of x and y:', np.union1d(x, y))
print()

# --------------------------------------------------------------- #

# We create an unsorted rank 1 ndarray
x = np.random.randint(1, 11, size=(10,))
print('x = ', x)

# We sort x and print the sorted array using sort as a function.
y = np.sort(x)
print('y = ', y)

# When we sort out of place the original array remains intact. To see this we print x again
x.sort()
print('sorted x = ', x)

# We sort x but only keep the unique elements in x
y = np.sort(np.unique(x))
print('unique values y = ', y)
print()

# --------------------------------------------------------------- #

# We create an unsorted rank 1 ndarray
x = np.random.randint(1, 11, size=(5, 5))
print('x = \n', x)

# We sort the columns of X and print the sorted array
y = np.sort(x, axis=1)
print('y = \n', y)

# We sort the rows of X and print the sorted array
y = np.sort(x, axis=0)
print('y = \n', y)
print()

# --------------------------------------------------------------- #

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1, 26).reshape(5, 5)
print('X = \n', X)

# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[(X % 2 != 0)]
print('Y = \n', Y)
