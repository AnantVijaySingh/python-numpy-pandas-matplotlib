# import NumPy into Python
import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0, 5001, size=(1000, 20))

# print the shape of X
print(X.shape)

# Now that you created the array we will mean normalize it. We will perform mean normalization using the following
# equation:
#
# Norm_Col𝑖=Col𝑖−𝜇𝑖𝜎𝑖
#
# where Col𝑖 is the 𝑖th column of 𝑋, 𝜇𝑖 is average of the values in the 𝑖th column of 𝑋, and 𝜎𝑖 is the
# standard deviation of the values in the 𝑖th column of 𝑋. In other words, mean normalization is performed by
# subtracting from each column of 𝑋 the average of its values, and then by dividing by the standard deviation of its
# values. In the space below, you will first calculate the average and standard deviation of each column of 𝑋.

# Average of the values in each column of X
ave_cols = X.mean(axis=0)

# Standard Deviation of the values in each column of X
std_cols = X.std(axis=0)

# Print the shape of ave_cols
print(ave_cols.shape)

# Print the shape of std_cols
print(std_cols.shape)


# Take advantage of Broadcasting to calculate the mean normalized version of 𝑋 in just one line of code using the
# equation above. Fill in the code below

# Mean normalize X
X_norm = (X - ave_cols) / std_cols

# Print the average of all the values of X_norm
print(X_norm.mean())

# Print the average of the minimum value in each column of X_norm
print(X_norm.min(axis=0).mean())

# Print the average of the maximum value in each column of X_norm
print(X_norm.max(axis=0).mean())


# We create a random permutation of integers 0 to 4
np.random.permutation(5)

# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
row_indices = np.random.permutation(X_norm.shape[0])


# Make any necessary calculations.
# You can save your calculations into variables to use later.

# Create a Training Set
X_train = X_norm[row_indices[0: int((len(row_indices)*0.6))]]

# Create a Cross Validation Set
X_crossVal = X_norm[row_indices[int((len(row_indices)*0.6)): int((len(row_indices)*0.8))]]

# Create a Test Set
X_test = X_norm[row_indices[int((len(row_indices)*0.8)):]]

# Print the shape of X_train
print(X_train.shape)

# Print the shape of X_crossVal
print(X_crossVal.shape)

# Print the shape of X_test
print(X_test.shape)
