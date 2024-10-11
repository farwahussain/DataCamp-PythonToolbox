#Task1 : Write Generator Expressions

#Create generator object: result
result = (num for num in range(0, 30))

#Print first 3 values using next()
print(next(result))
print(next(result))
print(next(result))

#Print rest of the list
for values in result:
    print(values)
    

#Task2 : create a generator object that you will iterate over to print its values.
print("------------------Task2---------------------")
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

lengths = (len(person) for person in lannister)

#Iterate over and print the values in lengths
for values in lengths:
    print(values)