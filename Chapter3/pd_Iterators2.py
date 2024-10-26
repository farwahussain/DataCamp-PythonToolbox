#Task 2 : In this exercise, you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.
import pandas as pd # type: ignore

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('WDICSV.csv', chunksize = 1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['Country Code'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Country Name'], df_pop_ceb['2022'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)