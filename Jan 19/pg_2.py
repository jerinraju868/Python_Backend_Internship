''' 
    Create a program that takes in user input and performs division
    using try-exceptblocks to catch any ZeroDivisionError exceptions that may occur 
'''

# try block
try: 

    # accepting the 1st input from the user and store in variable x
    x = float(input('Enter the 1st number :'))

    # accepting the 2nd input from the user and store in variable y
    y = float(input('Enter the 2nd number :'))
    
    # y divides x and result stored in the variable div
    div = x / y

    # printing the result
    print(f'Result : {div}')

# except block for catching the zero division error 
except ZeroDivisionError:

    # displaying the error to the user
    print('Zero Division Error........!')

# except block for catching the input errors
except:

    # print the input error message to the user
    print('`Input error`')