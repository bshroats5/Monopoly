import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Import the first data set
data_set1 = pd.read_csv('Monopoly_Sheet1.csv')

# Import the second data set
data_set2 = pd.read_csv('Monopoly_Sheet3.csv')

# Import the third data set
data_set3 = pd.read_csv('Monopoly_Simulator_Counts.csv')

# Combine the three data sets into one data frame
data_frame = pd.concat([data_set1, data_set2, data_set3])

# Save the combined data frame to a new CSV file
data_frame.to_csv('new_data.csv', index=True)

# creating the data visualizations
# Most landed on spaces
most_landed = data_frame.nlargest(10, 'Count')
sns.barplot(x='Count', y='Space Name', data=most_landed)
plt.title('Top 10 Most Landed On Spaces')
plt.show()

# Least landed on spaces
least_landed = data_frame.nsmallest(10, 'Count')
sns.barplot(x='Count', y='Space Name', data=least_landed)
plt.title('Top 10 Least Landed On Spaces')
plt.show()

# Spaces ranked from most landed on to the least
sorted_spaces = data_frame.sort_values('Count', ascending=False)
sns.barplot(x='Count', y='Space Name', data=sorted_spaces)
plt.title('Spaces Ranked From Most Landed On to Least')
plt.show()


