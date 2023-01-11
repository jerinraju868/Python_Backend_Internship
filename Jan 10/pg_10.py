''' Find the sum of all odd numbers between the rane given by user using while loop '''

# accepting the range from the user
n = int(input('Enter the range : '))

# inititalize a variable to store the sum
sum = 0

# loop for getting the number under the range n 
while n > 0:
 
    # condition for checking the odd number
    if n % 2 != 0:

        # odd numbers are added to sum and stored in sum 
        sum += n

    # decrement the n value
    n -= 1

# printing the sum  odd numbers
print('Sum of odd numbers  :', sum)