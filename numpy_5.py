import numpy as np

# ndarray[start:end]
# ndarray[start:]
# ndarray[:end]
# NOTE: When we perform slices on ndarrays and save them into new variables, as we did above, the data is not
# copied into the new variable.

# We create a 4 x 5 ndarray that contains integers from 0 to 19
x = np.arange(20).reshape((4, 5))
print('x = \n', x)

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
z = x[1:4, 2:6]
print('z = \n', z)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
w = x[1:, 2:5]
print('w = \n', w)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
y = x[0:3, 2:5]
print('y = \n', y)

# We select all the elements in the 3rd row
v = x[2:3, :]
print('v = \n', v)

# We select all the elements in the 3rd column
q = x[:, 2:3]  # Returns a rank 2 array
print('q = \n', q)

q = x[:, 2]  # Returns a rank 1 array
print('q = \n', q)
print()

# --------------------------------------------------------------- #

# We create a 4 x 5 ndarray that contains integers from 0 to 19
x = np.arange(20).reshape((4, 5))
print('x = \n', x)

# create a copy of the slice using the np.copy() function
z = np.copy(x[1:4, 2:5])
print('z = \n', z)

# We change the last element in z to 555
print(z.shape)
z[z.shape[0] - 1, z.shape[1] - 1] = 555

print('z = \n', z)
print('x = \n', x)  # Value of x does not change as z was a copy
print()

# --------------------------------------------------------------- #

# We create a 4 x 5 ndarray that contains integers from 0 to 19
x = np.arange(20).reshape((4, 5))
print('x = \n', x)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1, 3])
print('indices = ', indices)

# We use the indices ndarray to select the 2nd and 4th row of X
y = x[indices, :]
print('y = \n', y)

# We use the indices ndarray to select the 2nd and 4th column of X
z = x[:, indices]
print('z = \n', z)

# --------------------------------------------------------------- #

# We create a 5 x 5 ndarray that contains integers from 0 to 19
x = np.arange(25).reshape((5, 5))
print('x = \n', x)

# We print the elements in the main diagonal of X
z = np.diag(x)
print('z = \n', z)

# We print the elements above the main diagonal of X
y = np.diag(x, k=1)
print('y = \n', y)

# We print the elements above the main diagonal of X
y = np.diag(x, k=-1)
print('y = \n', y)

# --------------------------------------------------------------- #

# Create 3 x 3 ndarray with repeated values
x = np.array([[1, 2, 3], [5, 2, 8], [1, 2, 3]])
print('x = \n', x)

# We print the unique elements of X
z = np.unique(x)
print('z = \n', z)

