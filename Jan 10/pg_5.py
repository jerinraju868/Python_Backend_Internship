''' Python program to print all even/odd numbers in the range given by user '''

# accepting the range from the user
n = int(input('Enter the range : '))

# declearing an empty arrays to store the even number and odd number
even, odd = [],[]

# loop for finding the even/ odd number under the range
for i in range(n):

    # condition for checking the even number
    if i % 2 == 0:

        # even numbers are stored in even array by using the append()
        even.append(i)
    else:

        # odd numbers are stored in odd array using the append()
        odd.append(i)

# printing the even numbers
print('Even :', even)

# printing the odd numbers
print('Odd  :', odd)