
#Positional and labeled indexing
#Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions. In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.
#
#Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner']. That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!
#
#To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.
#
#This course introduces a lot of new concepts, so if you ever need a quick refresher, download the Pandas Cheat Sheet and keep it handy!
#
#Instructions
#0 XP
#Explore the DataFrame in the IPython Shell using election.head().
#Assign the row position of election.loc['Bedford'] to x.
#Assign the column position of election['winner'] to y.
#Hit 'Submit Answer' to print the boolean equivalence of the .loc and .iloc selections.


# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])

# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[ ['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())

######################################

# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties =election.loc['Perry' : 'Potter']

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry' :-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())

#####################################################################
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame
print(three_counties)

#############################################################
#Thresholding data
#In this exercise, we have provided the Pennsylvania election results and included a column called 'turnout' that contains the percentage of voter turnout per county. Your job is to prepare a boolean array to select all of the rows and columns where voter turnout exceeded 70%.
#
#As before, the DataFrame is available to you as election with the index set to 'county'.
#
#Instructions
#100 XP
#Create a boolean array of the condition where the 'turnout' column is greater than 70 and assign it to high_turnout.
#Filter the election DataFrame with the high_turnout array and assign it to high_turnout_df.
#Print the filtered DataFrame. This has been done for you, so hit 'Submit Answer' to see it!


# Create the boolean array: high_turnout
high_turnout = election.turnout>70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)

