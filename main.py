import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('D:\\data anaytics internship\\task2\\HousePricePrediction.xlsx')



#sameena
print(df)

# first few rows of the DataFrame
print(df.head())

# some basic statistics about the DataFrame
print(df.describe())

# Print a specific column
print(df['MSZoning'])

# Print unique values in the 'MSZoning' column
print(df['MSZoning'].unique())

# Print value counts in the 'MSZoning' column
print(df['MSZoning'].value_counts())

# Print rows where 'MSZoning' is 'RL'
print(df[df['MSZoning'] == 'RL'])

# Print rows with index 0 to 4
print(df.loc[0:4])

# Print the first row
print(df.iloc[0])

# Print the first 5 rows of 'MSZoning' and 'LotArea' columns
print(df[['MSZoning', 'LotArea']].head())

# Print info about the DataFrame
print(df.info())

