######################################################
#Reading DataFrames from multiple files
#When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.
#
#The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.
#
#The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).
#
#This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Pandas Cheat Sheet and keep it handy!
#
#Instructions
#100 XP
#Import pandas as pd.
#Read the file 'Bronze.csv' into a DataFrame called bronze.
#Read the file 'Silver.csv' into a DataFrame called silver.
#Read the file 'Gold.csv' into a DataFrame called gold.
#Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.

# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold =  pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())
########################################################
#Reading DataFrames from multiple files in a loop
#As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.
#
#Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.
#
#Here, you'll continue working with The Guardian's Olympic medal dataset.
#
#Instructions
#100 XP
#Instructions
#100 XP
#Create a list of file names called filenames with three strings 'Gold.csv', 'Silver.csv', & 'Bronze.csv'. This has been done for you.
#Use a for loop to create another list called dataframes containing the three DataFrames loaded from filenames:
#Iterate over filenames.
#Read each CSV file in filenames into a DataFrame and append it to dataframes by using pd.read_csv() inside a call to .append().
#Print the first 5 rows of the first DataFrame of the list dataframes. This has been done for you, so hit 'Submit Answer' to see the results.


# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())

####################################################################
#Combining DataFrames from multiple data files
##In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.
##
##Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.
##
##Instructions
##100 XP
##Construct a copy of the DataFrame gold called medals using the .copy() method.
##Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
##Rename the columns of medals by assigning new_labels to medals.columns.
##Create new columns 'Silver' and 'Bronze' in medals using silver['Total'] & bronze['Total'].
#Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())
