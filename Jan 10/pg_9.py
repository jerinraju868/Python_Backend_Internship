''' Find the sum of all even numbers between the range given by user '''

# accepting the range from the user
n = int(input('Enter the range : '))

# inititalize a variable to store the sum
sum = 0

# loop for getting the number under the range n
for i in range(n):
 
    # condition for checking the even number
    if i % 2 == 0:

        # even numbers are added to sum and stored in sum 
        sum += i

# printing the sum  even numbers
print('Sum of Even numbers  :', sum)
