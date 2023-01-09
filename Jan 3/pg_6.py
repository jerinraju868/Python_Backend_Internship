''' check the given number is even or not '''

num = int(input('ENTER A NUMBER : ')) #getting input from the user

# checking modulus of the number, if the modulus is zero then it is even otherwise it is odd number
if num % 2 == 0:
    print('The number',num, 'is even')

else:
    print('The number',num, 'is odd')