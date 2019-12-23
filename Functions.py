# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1=word1+'!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+'!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words=(shout1,shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2= shout_all('congratulations' , 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)


# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry]+=1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry]=1

# Print the populated dictionary
print(langs_count)
