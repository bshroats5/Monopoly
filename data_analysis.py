import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Import the first data set
data_set1 = pd.read_csv('Monopoly - Sheet3.csv')

# Import the second data set
data_set2 = pd.read_csv('Monopoly_Simulator_Counts.csv')

# Combine the two data sets into one data frame
df = pd.concat([data_set1, data_set2])

# Print the combined data frame
print(df)

# Save the combined data frame to a new CSV file
df.to_csv('new_data.csv', index=False)

# creating the data visualizations
# Most landed on spaces
most_landed = df.nlargest(10, 'Count of Space Name')
sns.scatterplot(x='Space Name', y='Count of Space Name', data=most_landed)
plt.title('Top 10 Most Landed On Spaces')
plt.show()

# Least landed on spaces
least_landed = df.nsmallest(10, 'Count of Space Name')
sns.barplot(x='Count of Space Name', y='Space Name', data=least_landed)
plt.title('Top 10 Least Landed On Spaces')
plt.show()

# Spaces ranked from most landed on to the least
sorted_spaces = df.sort_values('Count of Space Name', ascending=False)
sns.barplot(x='Count of Space Name', y='Space Name', data=sorted_spaces)
plt.title('Spaces Ranked From Most Landed On to Least')
plt.show()


