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