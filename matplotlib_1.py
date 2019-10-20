import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pokemon = pd.read_csv('pokemon.csv')
print(pokemon.shape)
print()
print(pokemon.head(100))
print()

base_color = sb.color_palette()[4]  # selects a color palette from the standard palette

"""
Chart 1: Number of pokemons introduced in each generation
"""
sb.countplot(x='generation_id', data=pokemon, color=base_color)
# Order and color are optional

plt.show()  # to display the charts

"""
Chart 2 with decreasing order. We could have done this manually by passing a list order=[5, 1, 3, 4, 2, 7, 6]
"""

base_color = sb.color_palette()[2]

order_by_generation = pokemon['generation_id'].value_counts().index
# value_count is a pd methos that provides values for each column and the index provides a list of indexs

sb.countplot(x='generation_id', data=pokemon, color=base_color, order=order_by_generation)
plt.show()

"""
Chart 3: Number of pokemons based on their primary types
"""

base_color = sb.color_palette()[1]

order_by_type = pokemon['type_1'].value_counts().index

sb.countplot(y='type_1', data=pokemon, color=base_color, order=order_by_type)
# Using y argument instead x to rotate the chart

# plt.xticks(rotation=90)  rotate x axis to prevent overlap in case of long names or large number of values
plt.show()

"""
For ordinal-type data, we probably want to sort the bars in order of the variables. While we could sort the levels 
by frequency like above, we usually care about whether the most frequent values are at high levels, low levels, 
etc. The best thing for us to do in this case is to convert the column into an ordered categorical data type. By 
default, pandas reads in string data as object types, and will plot the bars in the order in which the unique values 
were seen. By converting the data into an ordered type, the order of categories becomes innate to the feature, 
and we won't need to specify an "order" parameter each time it's required in a plot. 
"""

# this method requires pandas v0.21 or later
# level_order = ['Alpha', 'Beta', 'Gamma', 'Delta']
# ordered_cat = pd.api.types.CategoricalDtype(ordered = True, categories = level_order)
# df['cat_var'] = df['cat_var'].astype(ordered_cat)


"""
Chart 4: Number of pokemons based on their primary and secondary types together
"""

pokemon_tyes = pokemon.melt(id_vars=['id', 'species'], value_vars=['type_1', 'type_2'],
                            var_name='type_level', value_name='type').dropna()

print(pokemon_tyes.head())
print()

type_counts = pokemon_tyes['type'].value_counts()
type_order = type_counts.index

sb.countplot(y='type', data=pokemon_tyes, color=base_color, order=type_order)
plt.show()

"""
Chart 5: Proposition of pokemons based on their primary and secondary types together
"""

n_pokemon = pokemon.shape[0]  # Number of pokemons
max_type_count = type_counts[0]  # Max number of a type
max_prop = max_type_count / n_pokemon  # Max possible proportion for the chart
print(max_prop)

tick_props = np.arange(0.00, max_prop, 0.02)  # create a list of values with 0.02 step value
tick_names = ('{:0.2f}'.format(v) for v in tick_props)  # format values to 2 decimal places

sb.countplot(y='type', data=pokemon_tyes, color=base_color, order=type_order)
plt.xticks(tick_props * n_pokemon, tick_names)
plt.xlabel('proportions')
plt.show()

"""
Chart 6: Proposition and count of pokemons based on their primary and secondary types
"""

n_pokemon = pokemon.shape[0]  # Number of pokemons
max_type_count = type_counts[0]  # Max number of a type
max_prop = max_type_count / n_pokemon  # Max possible proportion for the chart
print(max_prop)

tick_props = np.arange(0.00, max_prop, 0.02)  # create a list of values with 0.02 step value
tick_names = ('{:0.2f}'.format(v) for v in tick_props)  # format values to 2 decimal places

sb.countplot(y='type', data=pokemon_tyes, color=base_color, order=type_order)
for i in range(type_counts.shape[0]):
    count = type_counts[i]
    pct_string = "{:0.1f}%".format(100 * count / n_pokemon)
    plt.text(count + 1, i, pct_string, va='center')
plt.show()

"""
Chart 7 Pie Chart: Proposition and count of pokemons based on their primary and secondary types
"""

# code for the pie chart seen above
sorted_counts = pokemon
plt.pie(sorted_counts, labels=sorted_counts.index, startangle=90,
        counterclock=False)
plt.axis('square')
plt.show()
