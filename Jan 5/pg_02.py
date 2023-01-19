''' Python Program to add two number using recursion '''

# declearing the function called add() by accepting 2 arguments
def add(x, y):

    # adding both x and y then stored in s
    s = x + y

    # return the result stored in s
    return s

# accepting 1st input from the user
a = int(input('Enter 1st number :'))

# accepting 2nd input from the user
b = int(input('Enter 2nd number :'))

# calling the add() funtion by passing the values stored in a and b
print('Sum is :',add(a,b))
