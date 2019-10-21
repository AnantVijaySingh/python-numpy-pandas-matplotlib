import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

"""
Notes: Violin Plots
There are a few ways of plotting the relationship between one quantitative and one qualitative variable, 
that demonstrate the data at different levels of abstraction. The violin plot is on the lower level of abstraction. 
For each level of the categorical variable, a distribution of the values on the numeric variable is plotted. The 
distribution is plotted as a kernel density estimate, something like a smoothed histogram.
"""
fuel_econ = pd.read_csv('fuel_econ.csv')
fuel_econ['trans_type'] = fuel_econ['trans'].apply(lambda x: x.split()[0])
fuelTypes = ['Regular Gasoline', 'Premium Gasoline']
fuel_econ['fuelType'] = fuel_econ['fuelType'].filter(fuelTypes)
print(fuel_econ.head())


sedan_classes = fuel_econ['VClass'].unique()  # List of unique values
vclasses = pd.api.types.CategoricalDtype(ordered=True, categories=sedan_classes)
# Converts object type to plain categorical type putting the classes in order of size so that sorting of levels is
# automatic and we won't need to send order parameter in visualization calls
fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses)


base_color = sb.color_palette()[0]
sb.violinplot(data=fuel_econ, x='VClass', y='displ', color=base_color)
plt.xticks(rotation=45)
plt.show()

# with quartile lines
base_color = sb.color_palette()[0]
sb.violinplot(data=fuel_econ, x='VClass', y='displ', color=base_color, inner='quartile')
plt.xticks(rotation=45)
plt.show()

"""
Notes: Box Plots 
A box plot is another way of showing the relationship between a numeric variable and a categorical variable. Compared to
the violin plot, the box plot leans more on summarization of the data, primarily just reporting 
a set of descriptive statistics for the numeric values on each categorical level. 
"""

sb.boxplot(data=fuel_econ, x='VClass', y='displ', color=base_color)
plt.xticks(rotation=45)
plt.show()

"""
Notes: Clustered Bar Charts
To depict the relationship between two categorical variables, we can extend the univariate bar chart seen in the 
previous lesson into a clustered bar chart. Like a standard bar chart, we still want to depict the count of data 
points in each group, but each group is now a combination of labels on two variables. 
"""

"""
Chart 1: Heatmap
"""

# Data summarization
# get data for number of cars for each trans type as a panda series
ct_counts = fuel_econ.groupby(['VClass', 'trans_type']).size()

# Reset the series into a dataframe
ct_counts = ct_counts.reset_index(name='count')

# Rearrange data to get VClass on rows, trans_type as columns and values as counts
ct_counts = ct_counts.pivot(index='VClass', columns='trans_type', values='count')

print(ct_counts.head())


sb.heatmap(ct_counts, annot=True, fmt='d')
plt.show()

"""
Chart 1: Clustered Bar Chart
"""

sb.countplot(data=fuel_econ, x='VClass', hue='trans_type')
plt.xticks(rotation=45)
plt.show()


"""
Notes: Faceting
One general visualization technique that will be useful for you to know about to handle plots of two or more 
variables is faceting. In faceting, the data is divided into disjoint subsets, most often by different levels of a 
categorical variable. For each of these subsets of the data, the same plot type is rendered on other variables. 
Faceting is a way of comparing distributions or relationships across levels of additional variables, especially when 
there are three or more variables of interest overall. 
"""
bins = np.arange(12, 58 + 2, 2)
graph = sb.FacetGrid(data=fuel_econ, col='VClass', col_wrap=3)
graph.map(plt.hist, 'comb', bins=bins)
plt.show()


"""
Notes: Adapted Bar Charts Bar Plots 
These plots can be adapted for use as bivariate plots by, instead of  indicating count by height, indicating a mean or
other statistic on a second variable. 
"""

base_color = sb.color_palette()[0]
# add ci ='sd' argument to get standard deviation plot
sb.barplot(data=fuel_econ, x='VClass', y='displ', color=base_color)
plt.xticks(rotation=45)
plt.show()


"""
Notes: Line Plots
The line plot is a fairly common plot type that is used to plot the trend of one numeric variable against values of a 
second variable. In contrast to a scatterplot, where all data points are plotted, in a line plot, only one point is 
plotted for every unique x-value or bin of x-values (like a histogram). If there are multiple observations in an 
x-bin, then the y-value of the point plotted in the line plot will be a summary statistic (like mean or median) of 
the data in the bin. The plotted points are connected with a line that emphasizes the sequential or connected nature 
of the x-values. 
"""

bins_e = np.arange(0.6, 7 + 0.2, 0.2)
bins_c = bins_e[:-1] + 0.1

displ_binned = pd.cut(fuel_econ['displ'], bins_e, include_lowest=True)
comb_mean = fuel_econ['comb'].groupby(displ_binned).mean()
# comb_std = fuel_econ['comb'].groupby(displ_binned.std())

plt.errorbar(x=bins_c, y='comb_mean')
plt.xlabel('Displacement')
plt.ylabel('Avg. Combined Fuel Efficiency (mpg)')
plt.show()
