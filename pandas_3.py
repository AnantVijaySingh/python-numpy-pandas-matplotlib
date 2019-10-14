import pandas as pd

# We create a dictionary of Pandas Series
items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
         'Alice': pd.Series(data=[40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}
# We print the type of items to see that it is a dictionary
print(type(items))
print()

# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_cart = pd.DataFrame(items)

# We display the DataFrame
print(shopping_cart)
print()

"""
NOTE: Also notice that the row labels of the DataFrame are built from the union of the index labels of the two
# Pandas Series we used to construct the dictionary. And the column labels of the DataFrame are taken from the keys
# of the dictionary.
"""

# --------------------------------------------------------------- #

# We create a dictionary of Pandas Series without indexes
data = {'Bob': pd.Series([245, 25, 55]),
        'Alice': pd.Series([40, 110, 500, 45])}

# We create a DataFrame
df = pd.DataFrame(data)
print(df)
print()

"""
NOTE: If we don't provide index labels to the Pandas Series, Pandas will use numerical row indexes when it creates the
DataFrame.
"""

# --------------------------------------------------------------- #

# We print some information about shopping_carts
print('shopping_carts has shape:', shopping_cart.shape)
print('shopping_carts has dimension:', shopping_cart.ndim)
print('shopping_carts has a total of:', shopping_cart.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_cart.values)
print()
print('The row index in shopping_carts is:', shopping_cart.index)
print()
print('The column index in shopping_carts is:', shopping_cart.columns)
print()

# --------------------------------------------------------------- #

# We Create a DataFrame that only has Bob's data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])
print("DataFrame that only has Bob's data:\n", bob_shopping_cart)
print()

# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index=['bike', 'books', 'glasses'])
print("DataFrame that only has selected items for both Alice and Bob:\n", sel_shopping_cart)
print()

# We Create a DataFrame that only has selected items for Alice
alice_shopping_cart = pd.DataFrame(items, index=['books', 'glasses'], columns=['Alice'])
print("DataFrame that only has selected items for Alice:\n", alice_shopping_cart)
print()

# --------------------------------------------------------------- #

# We create a dictionary of lists (arrays)
data = {'Integers': [1, 2, 3],
        'Floats': [4.5, 8.2, 9.6]}

# We create a DataFrame. Pandas will use numerical labels as we did not provide it any
df = pd.DataFrame(data)
print(df)
print()

# We create a DataFrame and provide the row index
df = pd.DataFrame(data, index=['label 1', 'label 2', 'label 3'])
print(df)
print()

# --------------------------------------------------------------- #

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

# We create a DataFrame
store_items = pd.DataFrame(items2)
print(store_items)
print()

# We create a DataFrame and provide the row index
store_items = pd.DataFrame(items2, index=['store 1', 'store 2'])
print(store_items)
print()
