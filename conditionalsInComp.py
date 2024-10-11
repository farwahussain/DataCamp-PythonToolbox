#Task-1 create a list that only includes the members of fellowship that have 7 characters or more

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

#conditionals in comprehension
new_fellowship = [member for member in fellowship if len(member) >= 7]

print(new_fellowship)

#Task-2 create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string

fellowship2 = [member if len(member) >= 7 else '' for member in fellowship]

print(fellowship2)