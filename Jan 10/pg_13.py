'''
    o
    1 2
    3 4 5
    6 7 8 9
'''

# accepting the input for no of rows from the user
n = int(input("Enter number of rows : "))

# initilizing a variable
x = 0

# loop for row
for i in range(1,n+1):

    # loop for column
    for j in range(1, i+1):

        # printing the number
        print(x, end=" ")

        # increment the number
        x += 1
    
    # next line
    print()