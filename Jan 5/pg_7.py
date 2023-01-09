''' Python Program to find sum of array elements '''

# accepting 1st array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# declearing a variable to store the sum of the array
s = 0

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

    # addtion operation is performed and stored in s 
    s += a[i]

# displaying the sum of the array stored
print('Sum of the array elements :', s)
