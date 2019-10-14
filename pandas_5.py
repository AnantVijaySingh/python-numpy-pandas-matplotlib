import pandas as pd
import numpy as np

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes': 8, 'suits': 45},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5, 'shirts': 2, 'shoes': 5, 'suits': 7},
          {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes': 10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index=['store 1', 'store 2', 'store 3'])

# We display the DataFrame
print(store_items)
print()

# We count the number of NaN values in store_items
NaN_DataFrame = store_items.isnull()
print(NaN_DataFrame)
print()
Sum_NaN_Per_Columns = store_items.isnull().sum()
print(Sum_NaN_Per_Columns)
print()
Total_NaN_Values = store_items.isnull().sum().sum()
print('Total NaN values: ', Total_NaN_Values)
print()

# We print the number of non-NaN values in our DataFrame
Non_NaN_Values = store_items.count().sum()
print('Non NaN values: ', Non_NaN_Values)

# --------------------------------------------------------------- #

# We drop any rows with NaN values
modified_store = store_items.dropna(axis=0, inplace=False)
print(modified_store)
print()

# We drop any columns with NaN values
modified_store = store_items.dropna(axis=1, inplace=False)
print(modified_store)
print()

# --------------------------------------------------------------- #

# We display the DataFrame
print(store_items)
print()

# We replace all NaN values with 0
modified_store = store_items.fillna(0)
print(modified_store)
print()

# We replace NaN values with the previous value in the column
modified_store = store_items.fillna(method='ffill', axis=0, inplace=False)
print(modified_store)
print()

# We replace NaN values with the previous value in the row
modified_store = store_items.fillna(method='ffill', axis=1, inplace=False)
print(modified_store)
print()

# We replace NaN values with the next value in the column
modified_store = store_items.fillna(method='backfill', axis=0, inplace=False)
print(modified_store)
print()

# We replace NaN values with the next value in the row
modified_store = store_items.fillna(method='backfill', axis=1, inplace=False)
print(modified_store)
print()

"""
The original DataFrame is not modified. You can always replace the NaN values in place by setting 
the keyword inplace = True inside the fillna() function.
"""

# --------------------------------------------------------------- #

# We replace NaN values by using linear interpolation using column values
modified_store = store_items.interpolate(method='linear', axis=0)
print(modified_store)
print()

# We replace NaN values by using linear interpolation using row values
store_items.interpolate(method='linear', axis=1)
print(modified_store)
print()

# --------------------------------------------------------------- #


# Since we will be working with ratings, we will set the precision of our
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame.

# Create a dictionary with the data given above
dat = {
    'books': books,
    'authors': authors,
    'user_1': user_1,
    'user_2': user_2,
    'user_3': user_3,
    'user_4': user_4
}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)
print(book_ratings)
print()

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:
avg_values = book_ratings.mean(axis=0)
print(avg_values)
book_ratings.fillna(value=avg_values, axis=0, inplace=True)
print(book_ratings)
print()

# From the DataFrame above you can now pick all the books that had a rating of 5.
is_five_rating = (book_ratings[['user_1', 'user_2', 'user_3', 'user_4']] == 5)

best_rated = book_ratings[(book_ratings['user_2'] == 5)].append(book_ratings[(book_ratings['user_1'] == 5)])
print(is_five_rating)
print(best_rated)
print()




