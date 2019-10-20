import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

"""
Notes: the trend looks like a log(y)∝xrelationship (that is, linear increases in the value of x are associated with 
linear increases in the log of y), plotting the regression line on the raw units is not appropriate.
"""

fuel_econ = pd.read_csv('fuel_econ.csv')
print(fuel_econ.head())

"""
Chart 1: Correlation with matplotlib pylot function
"""

plt.scatter(data=fuel_econ, x='displ', y='comb')
plt.xlabel('Displacement')
plt.ylabel('Combined Fuel Efficiency (mpg)')
plt.show()

"""
Chart 2: Correlation with seaborn regplot. This adds a regression line
"""

sb.regplot(data=fuel_econ, x='displ', y='comb')
plt.xlabel('Displacement')
plt.ylabel('Combined Fuel Efficiency (mpg)')
plt.show()

"""
Chart 3: Transformation to log scale for y axis
"""


def log_trans(x, inverse=False):
    if not inverse:
        return np.log10(x)
    else:
        return np.power(10, x)


sb.regplot(fuel_econ['displ'], fuel_econ['comb'].apply(log_trans))
tick_locs = [10, 20, 50, 100, 200, 500]
plt.yticks(log_trans(tick_locs), tick_locs)
plt.show()

"""
Notes: Overplotting can be caused when there are too many data points. In this case we can use sampling, transparency 
and jitter
"""

"""
Chart 4: Relationship between Fuel efficiency and year of make. Add transpareny and jitter to better understand the data
"""

sb.regplot(data=fuel_econ, x='year', y='comb')
plt.xlabel('Year of make')
plt.ylabel('Fuel Efficiency (mpg)')
plt.show()

"""
Chart 5: Relationship between Fuel efficiency and year of make. Add transpareny and jitter to better understand the data
"""

sb.regplot(data=fuel_econ, x='year', y='comb', x_jitter=0.3, scatter_kws={'alpha': 1 / 10})  # for matplotlip we can
# simply pass alpha as argument to the function
plt.xlabel('Year of make')
plt.ylabel('Fuel Efficiency (mpg)')
plt.show()

"""
Chart 7: Heat map for displacement and fuel efficiency
"""
# value of bins is selected based on fuel_econ['disp', 'comb'].describe() values to help understand what range to use
bins_x = np.arange(0.6, 7 + 0.3, 0.3)
bins_y = np.arange(12, 58 + 3, 3)

# viridis is the default palette which is dark. viridis_r is a reverse palette
# cmin set the min value a heat box must have to get a color
plt.hist2d(data=fuel_econ, x='displ', y='comb', cmin=0.5, cmap='viridis_r', bins=[bins_x, bins_y])

plt.colorbar()
plt.xlabel('Displacement')
plt.ylabel('Combined Fuel Efficiency (mpg)')
plt.show()

"""
Chart 8: Heat map with counts for displacement and fuel efficiency
"""
# value of bins is selected based on fuel_econ['disp', 'comb'].describe() values to help understand what range to use
bins_x = np.arange(0.6, 7 + 0.3, 0.3)
bins_y = np.arange(12, 58 + 3, 3)

# viridis is the default palette which is dark. viridis_r is a reverse palette
# cmin set the min value a heat box must have to get a color
h2d = plt.hist2d(data=fuel_econ, x='displ', y='comb', cmin=0.5, cmap='viridis_r', bins=[bins_x, bins_y])

plt.colorbar()

counts = h2d[0]

# loop through the cell counts and add text annotations for each
for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        c = counts[i, j]
        if c >= 7:  # increase visibility on darkest cells
            plt.text(bins_x[i] + 0.5, bins_y[j] + 0.5, int(c),
                     ha='center', va='center', color='white')
        elif c > 0:
            plt.text(bins_x[i] + 0.5, bins_y[j] + 0.5, int(c),
                     ha='center', va='center', color='black')

plt.xlabel('Displacement')
plt.ylabel('Combined Fuel Efficiency (mpg)')
plt.show()
