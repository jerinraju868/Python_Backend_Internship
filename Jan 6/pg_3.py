''' write a program to  check if element exists in list in Python	'''

# accepting array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

# accepting the element to check
e = int(input('Enter the element to search : '))

# loop for taking each elements
for i in range(0,n):
    
    # checking the current index element is same as the user need to be check
    if a[i] == e :

        # displaying the element location 
        print('Element is located in  position ', i+1)
        
        # exiting the loop if the element is found
        break
# if element is not present in the list else condition is executed
else:
    print('Sorry..!Element is not present in the list')