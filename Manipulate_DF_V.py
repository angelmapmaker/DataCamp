 
#Using .value_counts() for ranking
#For this exercise, you will use the pandas Series method .value_counts() to determine the top 15 countries ranked by total number of medals.
#
#Notice that .value_counts() sorts by values by default. The result is returned as a Series of counts indexed by unique entries from the original Series with values (counts) ranked in descending order.
#
#The DataFrame has been pre-loaded for you as medals.
#
#Instructions
#100 XP
#Extract the 'NOC' column from the DataFrame medals and assign the result to country_names. Notice that this Series has repeated entries for every medal (of any type) a country has won in any Edition of the Olympics.
#Create a Series medal_counts by applying .value_counts() to the Series country_names.
#Print the top 15 countries ranked by total number of medals won. This has been done for you, so hit 'Submit Answer' to see the result.

# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))


########################################################################
#Using .pivot_table() to count medals by type
#Rather than ranking countries by total medals won and showing that list, you may want to see a bit more detail. You can use a pivot table to compute how many separate bronze, silver and gold medals each country won. That pivot table can then be used to repeat the previous computation to rank by total medals won.
#
#In this exercise, you will use .pivot_table() first to aggregate the total medals by type. Then, you can use .sum() along the columns of the pivot table to produce a new column. When the modified pivot table is sorted by the total medals column, you can display the results from the last exercise with a bit more detail.
#
#Instructions
#100 XP
#Construct a pivot table counted from the DataFrame medals, aggregating by 'count'. Use 'NOC' as the index, 'Athlete' for the values, and 'Medal' for the columns.
#Modify the DataFrame counted by adding a column counted['totals']. The new column 'totals' should contain the result of taking the sum along the columns (i.e., use .sum(axis='columns')).
#Overwrite the DataFrame counted by sorting it with the .sort_values() method. Specify the keyword argument ascending=False.
#Print the first 15 rows of counted using .head(15). This has been done for you, so hit 'Submit Answer' to see the result
# Construct the pivot table: counted
counted = medals.pivot_table(aggfunc='count', index='NOC', columns='Medal', values='Athlete')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values('totals', ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))

###########################################################
#Applying .drop_duplicates()
#What could be the difference between the 'Event_gender' and 'Gender' columns? You should be able to evaluate your guess by looking at the unique values of the pairs (Event_gender, Gender) in the data. In particular, you should not see something like (Event_gender='M', Gender='Women'). However, you will see that, strangely enough, there is an observation with (Event_gender='W', Gender='Men').
#
#The duplicates can be dropped using the .drop_duplicates() method, leaving behind the unique observations. The DataFrame has been loaded as medals.
#
#Instructions
#100 XP
#Select the columns 'Event_gender' and 'Gender'.
#Create a dataframe ev_gen_uniques containing the unique pairs contained in ev_gen.
#Print ev_gen_uniques. This has been done for you, so hit 'Submit Answer' to see the result.


# Select columns: ev_gen
ev_gen = medals.loc[:,['Event_gender', 'Gender']]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)


###########################################################
#Finding possible errors with .groupby()
#You will now use .groupby() to continue your exploration. Your job is to group by 'Event_gender' and 'Gender' and count the rows.
#
#You will see that there is only one suspicious row: This is likely a data error.
#
#The DataFrame is available to you as medals.
#
#Instructions
#100 XP
#Group medals by 'Event_gender' and 'Gender'.
#Create a medal_count_by_gender DataFrame with a group count using the .count() method.
#Print medal_count_by_gender. This has been done for you, so hit 'Submit Answer' to view the result.

# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender' , 'Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)

#Locating suspicious data
#You will now inspect the suspect record by locating the offending row.
#
#You will see that, according to the data, Joyce Chepchumba was a man that won a medal in a women's event. That is a data error as you can confirm with a web search.
#
#Instructions
#100 XP
#Create a Boolean Series with a condition that captures the only row that has medals.Event_gender == 'W' and medals.Gender == 'Men'. Be sure to use the & operator.
#Use the Boolean Series to create a DataFrame called suspect with the suspicious row.
#Print suspect. This has been done for you, so hit 'Submit Answer' to see the result.
# Create the Boolean Series: sus
sus = medals.loc[(medals.Event_gender == 'W') & (medals.Gender == 'Men') ]

# Create a DataFrame with the suspicious row: suspect
suspect = sus

# Print suspect
print(suspect)
###########################################################
#Using .nunique() to rank by distinct sports
#You may want to know which countries won medals in the most distinct sports. The .nunique() method is the principal aggregation here. Given a categorical Series S, S.nunique() returns the number of distinct categories.
#
#Instructions
#100 XP
#Group medals by 'NOC'.
#Compute the number of distinct sports in which each country won medals. To do this, select the 'Sport' column from country_grouped and apply .nunique().
#Sort Nsports in descending order with .sort_values() and ascending=False.
#Print the first 15 rows of Nsports. This has been done for you, so hit 'Submit Answer' to see the result.
# Group medals by 'NOC': country_grouped
country_grouped = medals.groupby('NOC')

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))
