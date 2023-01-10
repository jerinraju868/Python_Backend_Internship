''' Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same '''

# receving 3 inputs from the user
a = int(input('Enter the 1st number :'))
b = int(input('Enter the 2nd number :'))
c = int(input('Enter the 3rd number :'))

# condition for the givien number are equal or not
if a == b == c:

    # printing all are equal numbers
    print('All are equal')

# condition for checking is greate from a and b
elif a > b :
    
    # checking for the greater number from a and c
    if a > c :

        # printing the greater is a
        print('Greater : ', a)
    
    else:

        # printing the greater is c
        print('Greater :', c)

# checking for the greater number from b and c
elif b > c :

    # if b greater then print b is greater
    print('Greater : ',b)
else:

    # print c is greater
    print('Greter :', c)