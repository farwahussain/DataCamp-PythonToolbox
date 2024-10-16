#Task 1 : Extract the time from time-stamped Twitter data.

import pandas as pd

df = pd.read_csv('tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)

#Task 2 : add a conditional expression to the list comprehension so that you only select the times in which entry[17:19] is equal to '19'. 

tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

print(tweet_clock_time)