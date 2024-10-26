#Task 1 : In this exercise, you will read a file in small DataFrame chunks with read_csv().

# Import the pandas package
import pandas as pd # type: ignore

# Initialize reader object: df_reader
df_reader = pd.read_csv('WDICSV.csv', chunksize = 10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))