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
