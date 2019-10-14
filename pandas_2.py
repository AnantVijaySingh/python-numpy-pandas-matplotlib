import pandas as pd
import numpy as np

# We create a Pandas Series that stores a grocery list of just fruits
fruits = pd.Series(data=[10, 6, 3], index=['apples', 'oranges', 'bananas'])

# We display the fruits Pandas Series
print(fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2)  # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2)  # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2)  # We multiply each item in fruits by 2
print()
print('fruits / 2:\n', fruits / 2)  # We divide each item in fruits by 2
print()

# --------------------------------------------------------------- #

# We import NumPy as np to be able to use the mathematical functions
# We print fruits for reference
print('Original grocery list of fruits:\n', fruits)

# We apply different mathematical functions to all elements of fruits
print()
print('EXP(X) = \n', np.exp(fruits))
print()
print('SQRT(X) = \n', np.sqrt(fruits))
print()
print('POWER(X) = \n', np.power(fruits, 2))

# --------------------------------------------------------------- #

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# --------------------------------------------------------------- #

# You can also apply arithmetic operations on Pandas Series of mixed data type provided that the arithmetic operation
# is defined for all data types in the Series, otherwise you will get an error.

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print('Original grocery list:\n ', groceries)
print()

print('Multiply by 2:\n ', groceries * 2)
print()

print('Divide by 2 but only for the compatible data types:\n ', groceries.loc[['eggs', 'apples']] / 2)
print()

# --------------------------------------------------------------- #

# Create a Pandas Series that contains the distance of some planets from the Sun.
# Use the name of the planets as the index to your Pandas Series, and the distance
# from the Sun as your data. The distance from the Sun is in units of 10^6 km

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth', 'Saturn', 'Mars', 'Venus', 'Jupiter']

# Create a Pandas Series using the above data, with the name of the planets as
# the index and the distance from the Sun as your data.
dist_planets = pd.Series(data=distance_from_sun, index=planets)
print(dist_planets)
print()

# Calculate the number of minutes it takes sunlight to reach each planet. You can
# do this by dividing the distance from the Sun for each planet by the speed of light.
# Since in the data above the distance from the Sun is in units of 10^6 km, you can
# use a value for the speed of light of c = 18, since light travels 18 x 10^6 km/minute.
time_light = dist_planets / 18
print(time_light)
print()

# Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[(time_light < 40)]
print(close_planets)
print()
