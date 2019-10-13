import numpy as np

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'Chocolate', 'Ice-cream'])

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'Hello', 'World'])

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 2 ndarray that only contains integers
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print('y = ', y)
print('y has dimensions:', y.shape)
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)
print()


# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We save x into the current directory as
np.save('my_array', x)

# We load the saved array from our current directory into variable y
z = np.load('my_array.npy')

print('z = ', z)
print('z has dimensions:', z.shape)
print('z is an object of type:', type(z))
print('The elements in z are of type:', z.dtype)
print()
