import numpy as np

# We create a 3 x 4 ndarray full of zeros.
x = np.zeros((3, 4))  # requires a tuple to define the number of rows and columns

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a 3 x 2 ndarray full of ones.
x = np.ones((2, 2))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a 2 x 3 ndarray full of fives.
x = np.full((2, 3), 5, dtype=float)  # Arguments (shape, constant value , dtype (optional) )

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a 5 x 5 Identity matrix.
x = np.eye(5)

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50 on its main diagonal
x = np.diag([10, 20, 30, 50])

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)  # only end argument is required. End is excluded during construction.

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray that has sequential integers from 4 to 9.
x = np.arange(4, 10)

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray that has evenly spaced integers from 1 to 11 in steps of 2.
x = np.arange(1, 12, 2)

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# Even though the np.arange() function allows for non-integer steps, such as 0.3, the output is usually inconsistent,
# due to the finite floating point precision. For this reason, in the cases where non-integer steps are required,
# it is usually better to use the function np.linspace().

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0, 25, 10)  # Endpoint in inclusive

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25, with 25 excluded.
x = np.linspace(0, 25, 10, endpoint=False)

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# The np.reshape(ndarray, new_shape) function converts the given ndarray into the specified new_shape. It is
# important to note that the new_shape should be compatible with the number of elements in the given ndarray.


# We create a rank 1 ndarray with sequential integers from 0 to 19
x = np.arange(0,20)

# We reshape x into a 4 x 5 ndarray
x = np.reshape(x, (4, 5))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# One great feature about NumPy, is that some functions can also be applied as methods. This allows us to apply
# different functions in sequence in just one line of code.

# We create a a rank 1 ndarray with sequential integers from 0 to 19 and reshape it to a 4 x 5 array
x = np.arange(1, 21).reshape((5, 4))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a rank 1 ndarray with 10 integers evenly spaced between 0 and 50, with 50 excluded. We then reshape it to
# a 5 x 2 ndarray
x = np.linspace(0, 50, 10, endpoint=False).reshape((5, 2))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
x = np.random.random((3, 3))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
x = np.random.randint(4, 15, size=(3, 2))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print()

# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
x = np.random.normal(0, 0.1, size=(1000, 1000))

print(x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print('The elements in x have a mean of:', x.mean())
print('The maximum value in x is:', x.max())
print('The minimum value in x is:', x.min())
print('x has', (x < 0).sum(), 'negative numbers')
print('x has', (x > 0).sum(), 'positive numbers')
print()


# Using the Built-in functions you learned about in the
# previous lesson, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)

X = np.arange(2, 33, 2).reshape((4, 4))
print(X)
