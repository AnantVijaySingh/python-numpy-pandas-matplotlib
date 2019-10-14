import pandas as pd

# We create a list of Python dictionaries
items = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

# We create a DataFrame and provide the row index
store_items = pd.DataFrame(items, index=['store 1', 'store 2'])

print(store_items)
print()

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
print()

"""
NOTE: It is important to know that when accessing individual elements in a DataFrame, as we did in the last example 
above, the labels should always be provided with the column label first, i.e. in the form dataframe[column][row]. 
"""

# --------------------------------------------------------------- #

# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2

store_items['shirts'] = [15, 2]
print(store_items)
print()

# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['shirts'] + store_items['pants']
print(store_items)
print()

# We create a dictionary from a list of Python dictionaries that will number of items at the new store
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index=['store 3'])

# We append store 3 to our store_items DataFrame
store_items = store_items.append(new_store, sort=True)

print(store_items)
print()

# We add a new column using data from particular rows in the watches column: stock stores 2 and 3 with new watches
# and you want the quantity of the new watches to be the same as the watches already in stock for those stores.
store_items['new watches'] = store_items['watches'][1:]

print(store_items)
print()

# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8, 5, 0])

print(store_items)
print()

# --------------------------------------------------------------- #

# We remove the new watches column
store_items.pop('new watches')

print(store_items)
print()

# We remove the watches and shoes columns
store_items = store_items.drop(['watches', 'shoes'], axis=1)

print(store_items)
print()

# We remove the store 2 and store 1 rows
store_items = store_items.drop(['store 2', 'store 1'], axis=0)

print(store_items)
print()

# --------------------------------------------------------------- #

# We change the column label bikes to hats
store_items = store_items.rename(columns={'bikes': 'hats'})

print(store_items)
print()

# We change the row label from store 3 to last store
store_items = store_items.rename(index={'store 3': 'last store'})

print(store_items)
print()

# We change the row index to be the data in the pants column
store_items = store_items.set_index(['pants'])

print(store_items)
print()
