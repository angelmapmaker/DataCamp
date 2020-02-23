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
