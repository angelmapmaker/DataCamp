#################################
#Pivoting a single variable
#Suppose you started a blog for a band, and you would like to log how many visitors you have had, and how many signed-up for your newsletter. To help design the tours later, you track where the visitors are. A DataFrame called users consisting of this information has been pre-loaded for you.
#
#Inspect users in the IPython Shell and make a note of which variable you want to use to index the rows ('weekday'), which variable you want to use to index the columns ('city'), and which variable will populate the values in the cells ('visitors'). Try to visualize what the result should be.
#
#For example, in the video, Dhavide used 'treatment' to index the rows, 'gender' to index the columns, and 'response' to populate the cells. Prior to pivoting, the DataFrame looked like this:
#
#   id treatment gender  response
#0   1         A      F         5
#1   2         A      M         3
#2   3         B      F         8
#3   4         B      M         9
#After pivoting:
#
#gender     F  M
#treatment      
#A          5  3
#B          8  9
#In this exercise, your job is to pivot users so that the focus is on 'visitors', with the columns indexed by 'city' and the rows indexed by 'weekday'.
#
#Instructions
#100 XP
#Instructions
#100 XP
#Pivot the users DataFrame with the rows indexed by 'weekday', the columns indexed by 'city', and the values populated with 'visitors'.
#Print the pivoted DataFrame. This has been done for you, so hit 'Submit Answer' to view the result.

##############################################################

xercise
Pivoting all variables
If you do not select any particular variables, all of them will be pivoted. In this case - with the users DataFrame - both 'visitors' and 'signups' will be pivoted, creating hierarchical column labels.

You will explore this for yourself now in this exercise.

Instructions
100 XP
Pivot the users DataFrame with the 'signups' indexed by 'weekday' in the rows and 'city' in the columns.
Print the new DataFrame. This has been done for you.
Pivot the users DataFrame with both 'signups' and 'visitors' pivoted - that is, all the variables. This will happen automatically if you do not specify an argument for the values parameter of .pivot().
Print the pivoted DataFrame. This has been done for you, so hit 'Submit Answer' to see the result.


 # Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday', columns='city')

# Print the pivoted DataFrame
print(pivot)

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday', columns='city',values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)
print(users)

#########################################
Stacking & unstacking I
You are now going to practice stacking and unstacking DataFrames. The users DataFrame you have been working with in this chapter has been pre-loaded for you, this time with a MultiIndex. Explore it in the IPython Shell to see the data layout. Pay attention to the index, and notice that the index levels are ['city', 'weekday']. So 'weekday' - the second entry - has position 1. This position is what corresponds to the level parameter in .stack() and .unstack() calls. Alternatively, you can specify 'weekday' as the level instead of its position.

Your job in this exercise is to unstack users by 'weekday'. You will then use .stack() on the unstacked DataFrame to see if you get back the original layout of users.

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))


# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0, 1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))
