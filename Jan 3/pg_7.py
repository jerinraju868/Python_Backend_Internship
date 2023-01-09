''' check the given number is amstrong or not '''

n =int(input('enter the number: ')) # getting input from the user

x = n # copying the value of 'num' to 'x' 
l = len(str(n)) # checking the length of the number(means how many digits 0,00,000,0000) and stored in 'y' 
s = 0 # declearing a new variable called 's' as 0

while n > 0: # checking for the number grater than 0
    d = n % 10 # taking the last digit of the number
    s += d**l # finding power of the last digit and adding into sum 
    n = n // 10 # removing last digit

# checking the user entered  number is same as to the result. if it same,then the number is amstrong
if x == s:
    print("The given number", x, "is armstrong number")
else:
    print("The given number", x, "is not armstrong number")