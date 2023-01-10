''' Find the factorial of a number taken as input using while loop '''

# accepting the inpute from the user
num = int(input('Enter the number :'))

#  declearing the variables fact  for storing the factorial result 
fact = 1

# declearing the variable i for looping
i = 1

# loop
while i <= num:

    # multiplying the fact with i
    fact *= i

    # decrement the variable i
    i += 1

# printing the result
print("factorial of ", num, " is :", fact)