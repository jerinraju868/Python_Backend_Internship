'''     
        o
		1 1
		2 2 2
		3 3 3 3 
'''

# accepting the input for no of rows from the user
n = int(input("Enter number of rows : "))

# initilizing a variable
x = 0

# loop for row
for i in range(1,n+1):

    # loop for column
    for j in range(1,i+1):

        # print the number
        print(x, end=' ')
    
    # increment the value
    x = x + 1

    # next line
    print()