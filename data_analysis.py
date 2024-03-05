import pandas as pd

# Import the first data set
data_set1 = pd.read_csv('Monopoly - Sheet1.csv')

# Import the second data set
data_set2 = pd.read_csv('Monopoly - Sheet3.csv')

# Import the third data set
data_set3 = pd.read_csv('Monopoly Simulator Counts.csv')

# Combine the three data sets into one data frame
data_frame = pd.concat([data_set1, data_set2, data_set3])

# Print the combined data frame
print(data_frame)

# Save the combined data frame to a new CSV file
data_frame.to_csv('new_monoploy_data.csv', index=False)

# Print the first 5 rows of the combined data frame
print(data_frame.head())