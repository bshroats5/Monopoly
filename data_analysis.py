import pandas as pd
import matplotlib.pyplot as plt


# Import the first data set
data_set1 = pd.read_csv('Monopoly_Sheet1.csv')

# Import the second data set
data_set2 = pd.read_csv('Monopoly_Sheet3.csv')

# Import the third data set
data_set3 = pd.read_csv('Monopoly_Simulator_Counts.csv')

# Combine the three data sets into one data frame
data_frame = pd.concat([data_set1, data_set2, data_set3])

# Print the combined data frame
print(data_frame)

# Save the combined data frame to a new CSV file
data_frame.to_csv('new_data.csv', index=True)

# Print the first 5 rows of the combined data frame
print(data_frame.head())

# Print the last 5 rows of the combined data frame
print(data_frame.tail())

# Print the summary statistics of the combined data frame
print(data_frame.describe())

# Print the shape of the combined data frame
print(data_frame.shape)

# Print the column names of the combined data frame
print(data_frame.columns)

# Print the index of the combined data frame
print(data_frame.index)

# Print the values of the combined data frame
print(data_frame.values)

# Print the index of the combined data frame
print(data_frame.index)

# Do some data visualization with seaborn
import seaborn as sns

# Do some data visualization with seaborn
sns.pairplot(data_frame)

# Show the plot
plt.show()

