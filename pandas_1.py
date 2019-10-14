# A Pandas series is a one-dimensional array-like object that can hold many data types, such as numbers or strings.
# One of the main differences between Pandas Series and NumPy ndarrays is that you can assign an index label to each
# element in the Pandas Series. In other words, you can name the indices of your Pandas Series anything you want.
# Another big difference between Pandas Series and NumPy ndarrays is that Pandas Series can hold data of different
# data types.

import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])

print(groceries)

# We print some information about Groceries
print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')

# We print the index and data of Groceries
print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)

# We check whether bananas is a food item (an index) in Groceries
x = 'banana' in groceries.index
print('Banana in groceries: ', x)

x = 'milk' in groceries.index
print('Banana in groceries: ', x)
print()

# We access elements in Groceries using index labels:

# We use a single index label
print('How many eggs do we need to buy:', groceries['eggs'])
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']])
print()

# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']])
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n', groceries[[0, 1]])
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]])
print()

# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])
print()

# --------------------------------------------------------------- #

# We display the original grocery list
print('Original groceries list: \n', groceries)
print()

# We change the number of eggs to 2
groceries['eggs'] = 12

# We display the changed grocery list
print('Modified Grocery List:\n', groceries)
print()

# --------------------------------------------------------------- #

# We display the original grocery list
print('Original Grocery List:\n', groceries)
print()

# We remove apples from our grocery list. The drop function removes elements out of place
print('We remove apples (out of place):\n', groceries.drop('apples'))
print()

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print('Grocery List after removing apples out of place:\n', groceries)
print()

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace=True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print('Grocery List after removing apples in place:\n', groceries)

