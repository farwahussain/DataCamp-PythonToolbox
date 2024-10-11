#create a list comprehension: square

square = [x**2 for x in range(1, 11)]
print(square)

#create a 5*5 matrix using list of lists: matrix

matrix = [[col for col in range(0, 5)] for row in range(0, 5)]
for row in matrix:
    print(row)