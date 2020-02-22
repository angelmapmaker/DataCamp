
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

#########################################################################
#Filtering columns using other columns
#The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate. This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would be too-close-to-call.
#
#Your job is to use boolean selection to filter the rows where the margin was less than 1. You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.
#
#The DataFrame has been pre-loaded for you as election.
#
#Instructions
#70 XP
#Import numpy as np.
#Create a boolean array for the condition where the 'margin' column is less than 1 and assign it to too_close.
#Convert the entries in the 'winner' column where the result was too close to call to np.nan.
#Print the output of election.info(). This has been done for you, so hit 'Submit Answer' to see the results.
#Show Answer (-70 XP)
#Hint
#To create a boolean array of the condition where some column 'a' of some DataFrame df is 0, you could use df['a'] == 0.
#To convert the entries of the 'winner' column, you need to first select it along with the too_close array using election.loc[]. Inside .loc[], too_close should be passed in before 'winner'.


# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election.margin<1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close,'winner'] = np.nan

# Print the output of election.info()
print(election.info())

#################################################
#Exercise
##Exercise
##Filtering using NaNs
##In certain scenarios, it may be necessary to remove rows and columns with missing data from a DataFrame. The .dropna() method is used to perform this action. You'll now practice using this method on a dataset obtained from Vanderbilt University, which consists of data from passengers on the Titanic.
##
##The DataFrame has been pre-loaded for you as titanic. Explore it in the IPython Shell and you will note that there are many NaNs. You will focus specifically on the 'age' and 'cabin' columns in this exercise. Your job is to use .dropna() to remove rows where any of these two columns contains missing data and rows where all of these two columns contain missing data.
##
##You'll also use the .shape attribute, which returns the number of rows and columns in a tuple from a DataFrame, or the number of rows from a Series, to see the effect of dropping missing values from a DataFrame.
##
##Finally, you'll use the thresh= keyword argument to drop columns from the full dataset that have less than 1000 non-missing values.
##
##Instructions
##100 XP
##Select the 'age' and 'cabin' columns of titanic and create a new DataFrame df.
##Print the shape of df. This has been done for you.
##Drop rows in df with how='any' and print the shape.
##Drop rows in df with how='all' and print the shape.
#Drop columns from the titanic DataFrame that have less than 1000 non-missing values by specifying the thresh and axis keyword arguments. Print the output of .info() from this.

# Select the 'age' and 'cabin' columns: df
df = titanic[['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())


