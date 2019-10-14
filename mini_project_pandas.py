import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# We load the Google stock data into a DataFrame
google_stock = pd.read_csv('GOOG.csv')

# We load the Apple stock data into a DataFrame
apple_stock = pd.read_csv('AAPL.csv')

# We load the Amazon stock data into a DataFrame
amazon_stock = pd.read_csv('AMZN.csv')

# We display the google_stock DataFrame
print(google_stock.head())

"""TODO: You will now join the three DataFrames above to create a single new DataFrame that contains all the Adj Close for 
all the stocks. Let's start by creating an empty DataFrame that has as row indices calendar days between 2000-01-01 
and 2016-12-31. We will use the pd.date_range() function to create the calendar dates first and then we will create a 
DataFrame that uses those dates as row indices: """

# We create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index=dates)

"""
TO DO: You will now join the the individual DataFrames, google_stock, apple_stock, and amazon_stock, to the all_stocks 
DataFrame. However, before you do this, it is necessary that you change the name of the columns in each of the three 
dataframes. This is because the column labels in the all_stocks dataframe must be unique. Since all the columns in 
the individual dataframes have the same name, Adj Close, we must change them to the stock name before joining them. 
In the space below change the column label Adj Close of each individual dataframe to the name of the corresponding 
stock. You can do this by using the pd.DataFrame.rename() function. 
"""

# Change the Adj Close column label to Google
google_stock = google_stock.rename(columns={'Adj Close': 'Google'})

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(columns={'Adj Close': 'Apple'})

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(columns={'Adj Close': 'Amazon'})

# We display the google_stock DataFrame to check if we changed the column names successfully
print()
print(amazon_stock.head())
print()

"""
Now that we have unique column labels, we can join the individual DataFrames to the all_stocks DataFrame. For this 
we will use the dataframe.join() function. The function dataframe1.join(dataframe2) joins dataframe1 with dataframe2. 
We will join each dataframe one by one to the all_stocks dataframe. Fill in the code below to join the dataframes, 
the first join has been made for you: 
"""

# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock[['Date', 'Google']].set_index('Date'))

# # We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock[['Date', 'Apple']].set_index('Date'))

# # We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock[['Date', 'Amazon']].set_index('Date'))
print(all_stocks)

# Check if there are any NaN values in the all_stocks dataframe
print('Number of null values: ', all_stocks.isnull().sum().sum())
print()

# Remove any rows that contain NaN values
all_stocks.dropna(axis=0, inplace=True)
print(all_stocks)

# Print the average stock price for each stock
print('Average stock price for each stock:\n', all_stocks.mean())
print()

# Print the median stock price for each stock
print('Median stock price for each stock:\n', all_stocks.median())
print()

# Print the standard deviation of the stock price for each stock
print('standard deviation stock price for each stock:\n', all_stocks.std())
print()

# Print the correlation between stocks
print('correlation stock price for each stock:\n', all_stocks.corr())
print()

# We compute the rolling mean using a 150-Day window for Google stock
rollingMean = all_stocks[['Google']].rolling(150).mean()
print(rollingMean)

# this allows plots to be rendered in the notebook
# We plot the Google stock data
plt.plot(all_stocks['Google'])

# We plot the rolling mean ontop of our Google stock data
plt.plot(rollingMean)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show()
