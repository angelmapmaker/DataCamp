#Reading in a data file
#Now that you have identified the method to use to read the data, let's try to read one file. The problem with real data such as this is that the files are almost never formatted in a convenient way. In this exercise, there are several problems to overcome in reading the file. First, there is no header, and thus the columns don't have labels. There is also no obvious index column, since none of the data columns contain a full date or time.
#
#Your job is to read the file into a DataFrame using the default arguments. After inspecting it, you will re-read the file specifying that there are no headers supplied.
#
#The CSV file has been provided for you as the variable data_file.
#
#Instructions
#100 XP
#Import pandas as pd.
#Read the file data_file into a DataFrame called df.
#Print the output of df.head(). This has been done for you. Notice the formatting problems in df.
#Re-read the data using specifying the keyword argument header=None and assign it to df_headers.
#Print the output of df_headers.head(). This has already been done for you. Hit 'Submit Answer' and see how this resolves the formatting issues.

# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv(data_file)

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv(data_file, header=None)

# Print the output of df_headers.head()



print(df_headers.head())

###################################################################33
#Re-assigning column names
#After the initial step of reading in the data, the next step is to clean and tidy it so that it is easier to work with.
#
#In this exercise, you will begin this cleaning process by re-assigning column names and dropping unnecessary columns.
#
#pandas has been imported in the workspace as pd, and the file NOAA_QCLCD_2011_hourly_13904.txt has been parsed and loaded into a DataFrame df. The comma separated string of column names, column_labels, and list of columns to drop, list_to_drop, have also been loaded for you.
#
#Instructions
#100 XP
#Convert the comma separated string column_labels to a list of strings using .split(','). Assign the result to column_labels_list.
#Reassign df.columns using the list of strings column_labels_list.
#Call df.drop() with list_to_drop and axis='columns'. Assign the result to df_dropped.
#Print df_dropped.head() to examine the result. This has already been done for you.

# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop,axis='columns')

# Print the output of df_dropped.head()
print(df_dropped.head())

###########################################################
#Cleaning and tidying datetime data
#In order to use the full power of pandas time series, you must construct a DatetimeIndex. To do so, it is necessary to clean and transform the date and time columns.
#
#The DataFrame df_dropped you created in the last exercise is provided for you and pandas has been imported as pd.
#
#Your job is to clean up the date and Time columns and combine them into a datetime collection to be used as the Index.
#
#Instructions
#70 XP
#Convert the 'date' column to a string with .astype(str) and assign to df_dropped['date'].
#Add leading zeros to the 'Time' column. This has been done for you.
#Concatenate the new 'date' and 'Time' columns together. Assign to date_string.
#Convert the date_string Series to datetime values with pd.to_datetime(). Specify the format parameter.
#Set the index of the df_dropped DataFrame to be date_times. Assign the result to df_clean.
#Show Answer (-70 XP)
#Hint
#First, you need to access the 'date' column of df_dropped with df_dropped['date']. Then, you should call the .astype(str) method on this to convert it to a string.
#To concatenate the new 'date' and 'Time' columns, first access them with df_dropped['date'] and df_dropped['Time']. You can then concatenate them by adding them together.
#Inside pd.to_datetime(), pass in the concatenated date_string Series and specify the format parameter to convert it to datetime.
#Use the .set_index() method to set the index of df_dropped to be date_times.
#
#Did you find this hint helpful?

   # Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string =  df_dropped['date'] +df_dropped['Time'].apply(str)

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

## Print the output of df_clean.head()
print(df_clean.head())


#################################################
#Cleaning the numeric columns
#The numeric columns contain missing values labeled as 'M'. In this exercise, your job is to transform these columns such that they contain only numeric values and interpret missing data as NaN.
#
#The pandas function pd.to_numeric() is ideal for this purpose: It converts a Series of values to floating-point values. Furthermore, by specifying the keyword argument errors='coerce', you can force strings like 'M' to be interpreted as NaN.
#
#A DataFrame df_clean is provided for you at the start of the exercise, and as usual, pandas has been imported as pd.
#
#Instructions
#100 XP
#Print the 'dry_bulb_faren' temperature between 8 AM and 9 AM on June 20, 2011.
#Convert the 'dry_bulb_faren' column to numeric values with pd.to_numeric(). Specify errors='coerce'.
#Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011.
#Convert the 'wind_speed' and 'dew_point_faren' columns to numeric values with pd.to_numeric(). Again, specify errors='coerce'


# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['201106200800':'201106200900', 'dry_bulb_faren'])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['201106200800':'201106200900', 'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'],errors='coerce')

###########################################################################################
#Signal min, max, median
#Now that you have the data read and cleaned, you can begin with statistical EDA. First, you will analyze the 2011 Austin weather data.
#
#Your job in this exercise is to analyze the 'dry_bulb_faren' column and print the median temperatures for specific time ranges. You can do this using partial datetime string selection.
#
#The cleaned dataframe is provided in the workspace as df_clean.
#
#Instructions
#100 XP
#Select the 'dry_bulb_faren' column and print the output of .median().
#Use .loc[] to select the range '2011-Apr':'2011-Jun' from dry_bulb_faren' and print the output of .median().
#Use .loc[] to select the month '2011-Jan' from 'dry_bulb_faren' and print the output of .median().
#

# Print the median of the dry_bulb_faren column
print(df_clean['dry_bulb_faren'].mean())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].median())


#######################################################################################33
#
#Signal variance
#You're now ready to compare the 2011 weather data with the 30-year normals reported in 2010. You can ask questions such as, on average, how much hotter was every day in 2011 than expected from the 30-year average?
#
#The DataFrames df_clean and df_climate from previous exercises are available in the workspace.
#
#Your job is to first resample df_clean and df_climate by day and aggregate the mean temperatures. You will then extract the temperature related columns from each - 'dry_bulb_faren' in df_clean, and 'Temperature' in df_climate - as NumPy arrays and compute the difference.
#
#Notice that the indexes of df_clean and df_climate are not aligned - df_clean has dates in 2011, while df_climate has dates in 2010. This is why you extract the temperature columns as NumPy arrays. An alternative approach is to use the pandas .reset_index() method to make sure the Series align properly. You will practice this approach as well.
#
#Instructions
#100 XP
#Downsample df_clean with daily frequency and aggregate by the mean. Store the result as daily_mean_2011.
#Extract the 'dry_bulb_faren' column from daily_mean_2011 as a NumPy array using .values. Store the result as daily_temp_2011. Note: .values is an attribute, not a method, so you don't have to use ().
#Downsample df_climate with daily frequency and aggregate by the mean. Store the result as daily_climate.
#Reset the index of daily_climate and extract the Temperature column. To do this, first reset the index of daily_climate using the .reset_index() method, and then use bracket slicing to access 'Temperature'. Store the result as daily_temp_climate


# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('d').mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index().Temperature

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())

########################################################################
#Sunny or cloudy
#On average, how much hotter is it when the sun is shining? In this exercise, you will compare temperatures on sunny days against temperatures on overcast days.
#
#Your job is to use Boolean selection to filter for sunny and overcast days, and then compute the difference of the mean daily maximum temperatures between each type of day.
#
#The DataFrame df_clean from previous exercises has been provided for you. The column 'sky_condition' provides information about whether the day was sunny ('CLR') or overcast ('OVC').
#
#Instructions 1/3
#35 XP
#1
#2
#3
#Get the cases in df_clean where the sky is clear. That is, when 'sky_condition' equals 'CLR', assigning to is_sky_clear.
#Use .loc[] to filter df_clean by is_sky_clear, assigning to sunny.
#Resample sunny by day ('D'), and take the max to find the maximum daily temperature.

# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean['sky_condition']=='CLR'

# Filter df_clean using is_sky_clear
sunny = df_clean.loc[is_sky_clear]

# Resample sunny by day then calculate the max
sunny_daily_max = sunny.resample('D').max()

# See the result
sunny_daily_max.head()


###
#Get the cases in df_clean where the sky is overcast. Using .str.contains(), find when 'sky_condition' contains 'OVC', assigning to is_sky_overcast.
#Use .loc[] to filter df_clean by is_sky_overcast, assigning to overcast.
#Resample overcast by day ('D'), and take the max to find the maximum daily temperature.

# Using df_clean, when does sky_condition contain 'OVC'?
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')

# Filter df_clean using is_sky_overcast
overcast = df_clean.loc[is_sky_overcast]

# Resample overcast by day then calculate the max
overcast_daily_max = overcast.resample('D').max()

# See the result
overcast_daily_max.head()


# From previous steps
is_sky_clear = df_clean['sky_condition']=='CLR'
sunny = df_clean.loc[is_sky_clear]
sunny_daily_max = sunny.resample('D').max()
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')
overcast = df_clean.loc[is_sky_overcast]
overcast_daily_max = overcast.resample('D').max()

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()

# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()

# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean-overcast_daily_max_mean)

###################################################
#In this exercise, your job is to plot the weekly average temperature and visibility as subplots. To do this, you need to first select the appropriate columns and then resample by week, aggregating the mean.
#
#In addition to creating the subplots, you will compute the Pearson correlation coefficient using .corr(). The Pearson correlation coefficient, known also as Pearson's r, ranges from -1 (indicating total negative linear correlation) to 1 (indicating total positive linear correlation). A value close to 1 here would indicate that there is a strong correlation between temperature and visibility.
#
#The DataFrame df_clean has been pre-loaded for you.
#
#Instructions
#100 XP
#Import matplotlib.pyplot as plt.
#Select the 'visibility' and 'dry_bulb_faren' columns and resample them by week, aggregating the mean. Assign the result to weekly_mean.
#Print the output of weekly_mean.corr().
#Plot the weekly_mean dataframe with .plot(), specifying subplots=True.


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean.loc[:,['visibility' , 'dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()
###########################################################

# From previous steps
is_sky_clear = df_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')
sunny_hours = resampled.sum()
total_hours = resampled.count()
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()


################################################3
#Heat or humidity
#Dew point is a measure of relative humidity based on pressure and temperature. A dew point above 65 is considered uncomfortable while a temperature above 90 is also considered uncomfortable.
#
#In this exercise, you will explore the maximum temperature and dew point of each month. The columns of interest are 'dew_point_faren' and 'dry_bulb_faren'. After resampling them appropriately to get the maximum temperature and dew point in each month, generate a histogram of these values as subplots. Uncomfortably, you will notice that the maximum dew point is above 65 every month!
#
#df_clean has been pre-loaded for you.
#
#Instructions
#100 XP
#Select the 'dew_point_faren' and 'dry_bulb_faren' columns (in that order). Resample by month and aggregate the maximum monthly temperatures. Assign the result to monthly_max.
#Plot a histogram of the resampled data with bins=8, alpha=0.5, and subplots=True.

# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean.loc[:,['dew_point_faren' , 'dry_bulb_faren']]

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist',bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()
