''' write a program to swap 2 numbers  '''

a = int(input('ENTER 1st NUMBER: ')) # getting 1st input and stores in a variable called 'a'
b = int(input('ENTER 2nd NUMBER: ')) # getting 2st input and stores in a variable called 'b'

# before swapping
print('\nbefore swapping')
print('a = ',a, '\nb = ', b)

#swapping
a,b = b,a

# printing the difference
print('\nafter swapping')
print('a = ',a, '\nb = ', b)

