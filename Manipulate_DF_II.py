#Changing index of a DataFrame
#As you saw in the previous exercise, indexes are immutable objects. This means that if you want to change or modify the index in a DataFrame, then you need to change the whole index. You will do this now, using a list comprehension to create the new index.
#
#A list comprehension is a succinct way to generate a list in one line. For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: cubes = [i**3 for i in range(10)]. This is equivalent to the following code:
#
#cubes = []
#for i in range(10):
#    cubes.append(i**3)
#Before getting started, print the sales DataFrame in the IPython Shell and verify that the index is given by month abbreviations containing lowercase characters.
#
#By the way, if you haven't downloaded it already, check out the Pandas Cheat Sheet. It includes an overview of the most important concepts, functions and methods and might come in handy if you ever need a quick refresher!
#
#Instructions
#100 XP
#Create a list new_idx with the same elements as in sales.index, but with all characters capitalized.
#Assign new_idx to sales.index.
#Print the sales dataframe. This has been done for you, so hit 'Submit Answer' and to see how the index changed.

# Create the list of new indexes: new_idx
new_idx = [x.upper() for x in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

#####################################################################33
#Changing index name labels
#Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.
#
#Similarly, if all the columns are related in some way, you can provide a label for the set of columns.
#
#To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).
#
#Instructions
#100 XP
#Assign the string 'MONTHS' to sales.index.name to create a name for the index.
#Print the sales dataframe to see the index name you just created.
#Now assign the string 'PRODUCTS' to sales.columns.name to give a name to the set of columns.
#Print the sales dataframe again to see the columns name you just created

# Assign the string 'MONTHS' to sales.index.name
sales.index.name='MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name='PRODUCTS'

# Print the sales dataframe again
print(sales)


#####################################################
#Extracting data with a MultiIndex
#In the video, Dhavide explained the concept of a hierarchical index, or a MultiIndex. You will now practice working with these types of indexes.
#
#The sales DataFrame you have been working with has been extended to now include State information as well. In the IPython Shell, print the new sales DataFrame to inspect the data. Take note of the MultiIndex!
#
#Extracting elements from the outermost level of a MultiIndex is just like in the case of a single-level Index. You can use the .loc[] accessor as Dhavide demonstrated in the video.
#
#Instructions
#100 XP
#Print sales.loc[['CA', 'TX']]. Note how New York is excluded.
#Print sales['CA':'TX']. Note how New York is included.

# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales['CA':'TX'])

#######################################################################
#Setting & sorting a MultiIndex
#In the previous exercise, the MultiIndex was created and sorted for you. Now, you're going to do this yourself! With a MultiIndex, you should always ensure the index is sorted. You can skip this only if you know the data is already sorted on the index fields.
#
#To get started, print the pre-loaded sales DataFrame in the IPython Shell to verify that there is no MultiIndex.
#
#Instructions
#100 XP
#Create a MultiIndex by setting the index to be the columns ['state', 'month'].
#Sort the MultiIndex using the .sort_index() method.
#Print the sales DataFrame. This has been done for you, so hit 'Submit Answer' to verify that indeed you have an index with the fields state and month!

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)

####################################################33333
#
#
#Using .loc[] with nonunique indexes
#As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row. Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique. To see an example of this, you will index your sales data by 'state' in this exercise.
#
#As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.
#
#Instructions
#100 XP
#Set the index of sales to be the column 'state'.
#Print the sales DataFrame to verify that indeed you have an index with state values.
#Access the data from 'NY' and print it to verify that you obtain two rows.


# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])

#############################################################
#Indexing multiple levels of a MultiIndex
#Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.
#
#Looking up data based on inner levels of a MultiIndex can be a bit trickier. The trickiest of all these lookups are when you want to access some inner levels of the index. In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice. You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:
#
#stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]
#Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).
#
#In this exercise, you will use your sales DataFrame to do some increasingly complex lookups. Remember that you can type sales.head() in the console to review the structure of the DataFrame!
#
#Instructions
#0 XP
#Look up data for New York ('NY') in month 1 in the sales DataFrame.
#Look up data for California and Texas ('CA', 'TX') in month 2.
#Access the inner index month and look up data for all states in month 2. Use (slice(None), 2) to extract all rows in month 2.
#Hint
#Use the .loc[] accessor on sales with ('NY', 1) to look up data for 'NY' in month 1.
#Use the .loc[] accessor on sales with (['CA', 'TX'], 2), : to look up data for 'CA' and 'TX' in month 2.
#Use the .loc[] accessor on sales with (slice(None), 2), : to look up data for all states in month 2.



# Look up data for NY in month 1 in sales: NY_month1
NY_month1 = sales.loc[('NY', 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]
