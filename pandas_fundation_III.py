df1 = pd.read_csv(filename)

df2 = pd.read_csv(filename, parse_dates=['Date'])

df3 = pd.read_csv(filename, index_col='Date', parse_dates=True)

#####################################################################
#
#####################################################################
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)  

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)
