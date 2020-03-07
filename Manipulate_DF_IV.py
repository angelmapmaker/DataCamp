#Grouping by multiple columns
#In this exercise, you will return to working with the Titanic dataset from Chapter 1 and use .groupby() to analyze the distribution of passengers who boarded the Titanic.
#
#The 'pclass' column identifies which class of ticket was purchased by the passenger and the 'embarked' column indicates at which of the three ports the passenger boarded the Titanic. 'S' stands for Southampton, England, 'C' for Cherbourg, France and 'Q' for Queenstown, Ireland.
#
#Your job is to first group by the 'pclass' column and count the number of rows in each class using the 'survived' column. You will then group by the 'embarked' and 'pclass' columns and count the number of passengers.
#
#The DataFrame has been pre-loaded as titanic.
#
#Instructions
#100 XP
#Group by the 'pclass' column and save the result as by_class.
#Aggregate the 'survived' column of by_class using .count(). Save the result as count_by_class.
#Print count_by_class. This has been done for you.
#Group titanic by the 'embarked' and 'pclass' columns. Save the result as by_mult.
#Aggregate the 'survived' column of by_mult using .count(). Save the result as count_mult.
#Print count_mult. This has been done for you, so hit 'Submit Answer' to view the result.

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult =  titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)
####################################################################
#Grouping by another series
#In this exercise, you'll use two data sets from Gapminder.org to investigate the average life expectancy (in years) at birth in 2010 for the 6 continental regions. To do this you'll read the life expectancy data per country into one pandas DataFrame and the association between country and region into another.
#
#By setting the index of both DataFrames to the country name, you'll then use the region information to group the countries in the life expectancy DataFrame and compute the mean value for 2010.
#
#The life expectancy CSV file is available to you in the variable life_fname and the regions filename is available in the variable regions_fname.
#
#Instructions
#100 XP
#Read life_fname into a DataFrame called life and set the index to 'Country'.
#Read regions_fname into a DataFrame called regions and set the index to 'Country'.
#Group life by the region column of regions and store the result in life_by_region.
#Print the mean over the 2010 column of life_by_region


# Read life_fname into a DataFrame: life
life = pd.read_csv(life_fname, index_col='Country')

# Read regions_fname into a DataFrame: regions
regions = pd.read_csv(regions_fname, index_col='Country')

# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())

##################################################################
#Computing multiple aggregates of multiple columns
#The .agg() method can be used with a tuple or list of aggregations as input. When applying multiple aggregations on multiple columns, the aggregated DataFrame has a multi-level column index.
#
#In this exercise, you're going to group passengers on the Titanic by 'pclass' and aggregate the 'age' and 'fare' columns by the functions 'max' and 'median'. You'll then use multi-level selection to find the oldest passenger per class and the median fare price per class.
#
#The DataFrame has been pre-loaded as titanic.
#
#Instructions
#100 XP
#Instructions
#100 XP
#Group titanic by 'pclass' and save the result as by_class.
#Select the 'age' and 'fare' columns from by_class and save the result as by_class_sub.
#Aggregate by_class_sub using 'max' and 'median'. You'll have to pass 'max' and 'median' in the form of a list to .agg().
#Use .loc[] to print all of the rows and the column specification ('age','max'). This has been done for you.
#Use .loc[] to print all of the rows and the column specification ('fare','median').


# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max' , 'median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:,('fare','median')])

############################################################
#Aggregating on index levels/fields
#If you have a DataFrame with a multi-level row index, the individual levels can be used to perform the groupby. This allows advanced aggregation techniques to be applied along one or more levels in the index and across one or more columns.
#
#In this exercise you'll use the full Gapminder dataset which contains yearly values of life expectancy, population, child mortality (per 1,000) and per capita gross domestic product (GDP) for every country in the world from 1964 to 2013.
#
#Your job is to create a multi-level DataFrame of the columns 'Year', 'Region' and 'Country'. Next you'll group the DataFrame by the 'Year' and 'Region' levels. Finally, you'll apply a dictionary aggregation to compute the total population, spread of per capita GDP values and average child mortality rate.
#
#The Gapminder CSV file is available as 'gapminder.csv'.
#
#Instructions
#100 XP
#Read 'gapminder.csv' into a DataFrame with index_col=['Year','region','Country']. Sort the index.
#Group gapminder with a level of ['Year','region'] using its level parameter. Save the result as by_year_region.
#Define the function spread which returns the maximum and minimum of an input series. This has been done for you.
#Create a dictionary with 'population':'sum', 'child_mortality':'mean' and 'gdp':spread as aggregator. This has been done for you.
#Use the aggregator dictionary to aggregate by_year_region. Save the result as aggregated.
#Print the last 6 entries of aggregated. This has been done for you, so hit 'Submit Answer' to view the result.
#


# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder.csv',index_col=['Year','region','Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level=['Year','region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))


##############################################################
#Grouping on a function of the index
#Groupby operations can also be performed on transformations of the index values. In the case of a DateTimeIndex, we can extract portions of the datetime over which to group.
#
#In this exercise you'll read in a set of sample sales data from February 2015 and assign the 'Date' column as the index. Your job is to group the sales data by the day of the week and aggregate the sum of the 'Units' column.
#
#Is there a day of the week that is more popular for customers? To find out, you're going to use .strftime('%a') to transform the index datetime values to abbreviated days of the week.
#
#The sales data CSV file is available to you as 'sales.csv'.
#
#Instructions
#100 XP
#Read 'sales.csv' into a DataFrame with index_col='Date' and parse_dates=True.
#Create a groupby object with sales.index.strftime('%a') as input and assign it to by_day.
#Aggregate the 'Units' column of by_day with the .sum() method. Save the result as units_sum.
#Print units_sum. This has been done for you, so hit 'Submit Answer' to see the result.

# Read file: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)

#######################################################################3
#Detecting outliers with Z-Scores
#As Dhavide demonstrated in the video using the zscore function, you can apply a .transform() method after grouping to apply a function to groups of data independently. The z-score is also useful to find outliers: a z-score value of +/- 3 is generally considered to be an outlier.
#
#In this example, you're going to normalize the Gapminder data in 2010 for life expectancy and fertility by the z-score per region. Using boolean indexing, you will filter for countries that have high fertility rates and low life expectancy for their region.
#
#The Gapminder DataFrame for 2010 indexed by 'Country' is provided for you as gapminder_2010.
#
#Instructions
#100 XP
#Import zscore from scipy.stats.
#Group gapminder_2010 by 'region' and transform the ['life','fertility'] columns by zscore.
#Construct a boolean Series of the bitwise or between standardized['life'] < -3 and standardized['fertility'] > 3.
#Filter gapminder_2010 using .loc[] and the outliers Boolean Series. Save the result as gm_outliers.
#Print gm_outliers. This has been done for you, so hit 'Submit Answer' to see the results.

# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby([ 'region'])['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)

###################################################################
#Filling missing data (imputation) by group
#Many statistical and machine learning packages cannot determine the best action to take when missing data entries are encountered. Dealing with missing data is natural in pandas (both in using the default behavior and in defining a custom behavior). In Chapter 1, you practiced using the .dropna() method to drop missing values. Now, you will practice imputing missing values. You can use .groupby() and .transform() to fill missing data appropriately for each group.
#
#Your job is to fill in missing 'age' values for passengers on the Titanic with the median age from their 'gender' and 'pclass'. To do this, you'll group by the 'sex' and 'pclass' columns and transform each group with a custom function to call .fillna() and impute the median value.
#
#The DataFrame has been pre-loaded as titanic. Explore it in the IPython Shell by printing the output of titanic.tail(10). Notice in particular the NaNs in the 'age' column.
#
#Instructions
#100 XP
#Group titanic by 'sex' and 'pclass'. Save the result as by_sex_class.
#Write a function called impute_median() that fills missing values with the median of a series. This has been done for you.
#Call .transform() with impute_median on the 'age' column of by_sex_class.
#Print the output of titanic.tail(10). This has been done for you - hit 'Submit Answer' to see how the missing values have now been imputed.

# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex','pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())


# Impute age and assign to titanic['age']
titanic.age = by_sex_class['age'].transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))

###########################################3
#Other transformations with .apply
#The .apply() method when used on a groupby object performs an arbitrary function on each of the groups. These functions can be aggregations, transformations or more complex workflows. The .apply() method will then combine the results in an intelligent way.
#
#In this exercise, you're going to analyze economic disparity within regions of the world using the Gapminder data set for 2010. To do this you'll define a function to compute the aggregate spread of per capita GDP in each region and the individual country's z-score of the regional per capita GDP. You'll then select three countries - United States, Great Britain and China - to see a summary of the regional GDP and that country's z-score against the regional mean.
#
#The 2010 Gapminder DataFrame is provided for you as gapminder_2010. Pandas has been imported as pd.
#
#The following function has been defined for your use:
#
#def disparity(gr):
#    # Compute the spread of gr['gdp']: s
#    s = gr['gdp'].max() - gr['gdp'].min()
#    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
#    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
#    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
#    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})
#Instructions
#100 XP
#Instructions



#100 XP
#Group gapminder_2010 by 'region'. Save the result as regional.
#Apply the provided disparity function on regional, and save the result as reg_disp.
#Use .loc[] to select ['United States','United Kingdom','China'] from reg_disp and print the results.

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])


<script.py> output:
                      z(gdp)  regional spread(gdp)
    Country                                       
    United States   3.013374               47855.0
    United Kingdom  0.572873               89037.0
    China          -0.432756               96993.0

