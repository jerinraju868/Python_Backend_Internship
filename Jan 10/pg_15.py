''' 
        *
		* *
		* * *
		* * * *
'''

# accepting the input for no of rows from the user
n = int(input("Enter number of rows : "))

# loop for row
for i in range(1,n+1):

    # loop for column
    for j in range(1,i+1):

        # print the star
        print('*', end=' ')

    # next line
    print()