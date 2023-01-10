''' Python program to check the number taken as an input is even or odd,
    print invalide input if user enters anything other than integers
'''

# try block for checking the valid input
try:

    # accepting input from the user
    n = int(input('Enter a number : '))

    # checking the number is even or by taking the remainder
    if n % 2 == 0:

        # print the number is even
        print('The number is even ')
    
    # this statement executes when the remainder in non zero 
    else:

        # print the number is odd
        print('The number is odd')

# exception block 
except:

    # printing the error message as invalid input
    print('invalide input')