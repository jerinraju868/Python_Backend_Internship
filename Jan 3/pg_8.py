''' check the given number is palindrome or not  '''

num = int(input('Enter the number : ')) # getting input from the user

temp = num # copying the num value to temparory variable
rev = 0 # declearing new variable

while num>0 : # checking the num is greater than 0
    dig = num % 10 # taking last digit 
    rev = rev * 10 + dig # rev multiply whit 10 and add with last digit
    num = num // 10 # removing lst digit from the num

# checking wheather that the first entered number and the result is same. if same then it is palindrom
if( temp == rev ):
    print("The number", temp ,"is palindrome!")
else:
    print("The number", temp ,"is not a palindrome!")