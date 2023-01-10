''' Find the factorial of a number taken as input using for loop '''

# getting input from the user
num = int(input("enter a number: "))

# declearing the variable fact to store the factoiral result
fact = 1

# loop range from 1 to last_number+ 1
for i in range(1, num + 1):
    
    # finding the factorial
    fact = fact * i

# printing the result
print("factorial of ", num, " is", fact)