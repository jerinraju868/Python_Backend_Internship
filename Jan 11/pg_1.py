'''  Write a function to return even numbers from a list  '''

# defining a function and passing argument
def even(*args):

    # declearing an empty array
    even = []

    # loop for taking the all values under the range 
    for i in range(len(a)):
        
        # checking the reminder for each element if 0 then it is even number else odd
        if a[i] % 2 == 0:

            # even number is adding to another list by using the append()
            even.append(a[i])
        
    # return the even number stored array
    return even

# accepting the list size from the user
n =  int(input('Enter the list size : '))

# declearing an empty array
a = []

# loop for accp=epting and storing the list elements
for i in range(n):

    # adding the elements to array
    a.append(int(input("Enter value : ")))

# calling the even function and stores the value in result
result = even(a)

# displaying the result
print('Even numbers from the list :', result)