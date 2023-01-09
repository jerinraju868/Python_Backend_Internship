''' find the largest of 2 numbers  '''

a = int(input('ENTER 1st NUMBER : ')) # getting 1st input from the user 
b = int(input('ENTER 2nd NUMBER : ')) # getting 2nd input from the user

# creating a function large
def large(a,b):
    if a > b :
        return a # return a as greater
    else:
        return b # return b as greater
    
print('largest number is : ', large(a,b)) # printing largest number by calling function large