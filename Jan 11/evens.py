from even_module import even

# accepting the list size from the user
n =  int(input('Enter the list size : '))

# declearing an empty array
a = []

# loop for accp=epting and storing the list elements
for i in range(n):

    # adding the elements to array
    a.append(int(input("Enter value : ")))

# calling the even function and stores the value in result
result = even(n,a)

# displaying the result
print('Even numbers from the list :', result)