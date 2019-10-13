import numpy as np

# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.arange(1, 6)
print(x)

# Let's access some elements with positive indices
print('This is second element in x:', x[1])

# Let's access the same elements with negative indices
print('This is the second element', x[-4])
print()

# --------------------------------------------------------------- #

# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.arange(1, 6)
print(x)

# We change the fourth element in x from 4 to 20
x[3] = 20
print('Modified:\n x = ', x)
print()

# --------------------------------------------------------------- #

# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
x = np.arange(1, 10, 1).reshape((3, 3))
print(x)

# Let's access some elements in x
print('This is (1,2) element in x:', x[1, 2])

# We change the (0,0) element in x from 1 to 20
x[0, 0] = 20
print('Modified:\n x = ', x)
print()

# --------------------------------------------------------------- #

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])
print(x)

# We delete the first and last element of x
x = np.delete(x, [0, len(x) - 1])
print('Modified x = ', x)
print()

# --------------------------------------------------------------- #

# We create a rank 2 ndarray
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(y)

# We delete the first row of y
w = np.delete(y, 0, axis=0)
print('w = \n', w)

# We delete the first and last column of y
v = np.delete(y, [0, 2], axis=1)
print('v = \n', v)
print()

# --------------------------------------------------------------- #

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])
print('x = ', x)

# We append the integer 6 to x
x = np.append(x, 6)
print('x = ', x)

# We append the integer 7 and 8 to x
x = np.append(x, [7, 8])
print('x = ', x)
print()

# --------------------------------------------------------------- #

# We create a rank 2 ndarray
y = np.array([[1, 2, 3], [4, 5, 6]])
print('Original Y = \n', y)

# We append a new row containing 7,8,9 to y
v = np.append(y, [[7, 8, 9]], axis=0)
print('v = \n', v)

# We append a new column containing 9 and 10 to y
w = np.append(y, [[9], [10]], axis=1)
print('w = \n', w)
print()

# --------------------------------------------------------------- #

# np.insert(ndarray, index, elements, axis)

# We create a rank 1 ndarray
x = np.array([1, 2, 5, 6, 7])
print('Original x = ', x)

# We insert the integer 3 and 4 between 2 and 5 in x
x = np.insert(x, 2, [3, 4])
print('x = ', x)
print()

# --------------------------------------------------------------- #

# We create a rank 2 ndarray
y = np.array([[1, 2, 3], [7, 8, 9]])
print('Original Y = \n', y)

# We insert a row between the first and last row of y
v = np.insert(y, 1, [4, 5, 6], axis=0)
print('v = \n', v)

# We insert a column full of 5s between the first and second column of y
w = np.insert(y, 1, 5, axis=1)
print('w = \n', w)
print()

# --------------------------------------------------------------- #
# We create a rank 1 ndarray
x = np.array([1, 2])
print('Original x = \n', x)

# We create a rank 2 ndarray
y = np.array([[3, 4], [5, 6]])
print('Original y = \n', y)

# We stack x on top of Y
z = np.vstack((x, y))
print('z = \n', z)

# We stack x on the right of Y. We need to reshape x in order to stack it on the right of Y.
q = np.hstack((x.reshape(2, 1), y))
print('q = \n', q)



