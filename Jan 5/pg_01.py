'''Python Program to find sum of digit of number using recursion '''

# declearing the sum function with the argument accepting
def sum(n):

    # checking for single digit number
    if n < 10:

        # sum of single digit always the same number, so return the same number
        return n

    # if not a sing digit
    else:

        # declearing a variable to store the sum of digits in a number
        s = 0

        # checking for the number is greater than zero, if it, then the loop executes untill the condition become false
        while n > 0:

            # taking the remainder from the number
            r = n % 10
            
            # adding the remainder nummber to s
            s += r 

            # removing the last digit from the number
            n = n // 10

        # returns the result is stored in the variable s
        return s

# taking input from the user  
num = int(input('Enter the number : '))

# calling the sum() funciton
print('Sum of digits of the number is : ', sum(num))
