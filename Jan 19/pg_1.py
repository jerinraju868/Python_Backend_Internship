'''
    Write a program that takes in user input and checks if it is a valid integer. 
    If the input is not a valid integer, raise a custom exception with a message "Invalid input: Not aninteger."
'''

# try block 
try:
    
    # declearing a variable x for storing the user input
    x = int(input('Enter the interger : '))

    # priting the message  as valid input
    print('Valid integer')
        
# except block for handling the errors
except:

    # printing the error message to the user
    print('Invalid input: Not an integer.')