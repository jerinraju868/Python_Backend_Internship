''' Find the sum of all odd numbers between the rane given by user using while loop '''

# accepting the range from the user
n = int(input('Enter the range : '))

# inititalize a variable to store the sum
sum = 0

# loop for getting the number under the range n
for i in range(n):
 
    # condition for checking the odd number
    if i % 2 != 0:

        # odd numbers are added to sum and stored in sum 
        sum += i

# printing the sum  odd numbers
print('Sum of odd numbers  :', sum)