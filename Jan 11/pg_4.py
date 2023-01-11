''' 
    Write a Python function to multiply all the numbers in a list
        Sample List : (8, 2, 3, -1, 7)
        Expected Output : -336
'''

# defining the multiply function with accepting arguments
def multiply(a):

    # declearing a variable mul with value 1
    mul = 1

    # loop for taking the each elements from the array
    for i in range(len(a)):

        # multiplying the each list elements adn stores in mul variable
        mul *= a[i]
    
    # return the mul values
    return mul

# accepting the list size from the user
n =  int(input('Enter the list size : '))

# declearing an empty array
a = []

# loop for accepting and storing the list elements
for i in range(n):

    # adding the elements to array
    a.append(int(input("Enter value : ")))

# declearing object for calling the multiply function and stores the value in object
obj = multiply(a)

# display the value from the object
print('Multiplication :', obj)