''' write a program to find the factorial of a number '''

num = int(input('enter a number: ')) # getting input from the user

# creating a function fact to find factorial 
def fact(n):
    if (n==1 or n==0): # checking for the number is 0 or 1 
        return 1 # factorial for the numbers 0 and 1 is 1
    else:
        return n * fact(n - 1) 

# printing and calling the fact function
print("Factorial of",num,"is",fact(num))
