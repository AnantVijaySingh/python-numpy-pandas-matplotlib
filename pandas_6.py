import pandas as pd

# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('goog-1.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)
print()

# Checking just the first or last few rows of a large dataset
print(Google_stock.head())
print()
print(Google_stock.tail())
print()

# Check whether we have any NaN values in our dataset
null_values = Google_stock.isnull().any()
print('Are there any null values: ', null_values)
print()

# We get descriptive statistics on our stock data
description = Google_stock.describe()
print(description)
print()

# We get descriptive statistics on a single column of our DataFrame
adjClose_desc = Google_stock['Adj Close'].describe()
print(adjClose_desc)
print()

# We print information about our DataFrame
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())
print()

# We display the correlation between columns
correlation = Google_stock.corr()
print(correlation)
print()


# --------------------------------------------------------------- #


# We load fake Company data in a DataFrame
data = pd.read_csv('test_company_data.csv')

print(data)
print()

# We display the total amount of money spent in salaries each year
total_per_year = data.groupby(['Year'])['Salary'].sum()
print('total amount of money spent in salaries each year:\n', total_per_year)
print()

# We display the average salary per year
avg_salary = data.groupby(['Year'])['Salary'].mean()
print('average salary per year:\n', avg_salary)
print()

# We display the salary distribution per department per year.
salary_dept_year = data.groupby(['Year', 'Department'])['Salary'].sum()
print('salary distribution per department per year:\n', salary_dept_year)
print()
