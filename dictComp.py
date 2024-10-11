#create a dictionary with the members of the list as the keys and the length of each string as the corresponding values.

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = { member: len(member) for member in fellowship}

print(new_fellowship)