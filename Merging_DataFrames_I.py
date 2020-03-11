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

##########################################################
#Sorting DataFrame with the Index & columns
#It is often useful to rearrange the sequence of the rows of a DataFrame by sorting. You don't have to implement these yourself; the principal methods for doing this are .sort_index() and .sort_values().
#
#In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.
#
#Instructions
#100 XP
#Read 'monthly_max_temp.csv' into a DataFrame called weather1 with 'Month' as the index.
#Sort the index of weather1 in alphabetical order using the .sort_index() method and store the result in weather2.
#Sort the index of weather1 in reverse alphabetical order by specifying the additional keyword argument ascending=False inside .sort_index().
#Use the .sort_values() method to sort weather1 in increasing numerical order according to the values of the column 'Max TemperatureF'.
# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 =  weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values(by='Max TemperatureF' )

# Print the head of weather4
print(weather4.head())




