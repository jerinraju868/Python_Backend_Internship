''' Python program to print the multiplication table of any number
    (number should be taken as input and user decides the end limit of the table)
'''

# accepting the input from the user
x = int(input('Enter the number : '))

# accepting the limit from the user
n = int(input('Enter the limit for the multiplication : '))

# loop for multiply the number 
for i in range(0,n+1):

    # printing the multipication table
    print(i, '*', x, '=', i*x)