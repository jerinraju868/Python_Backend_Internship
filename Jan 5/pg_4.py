''' Python program to perform right rotation in array by 2 positions '''

# accepting the size of an array from user
n = int(input('Array size : '))

# declearing an empty array
a = []

# declearing a variable for no of rotations to be  applied
sr = 2

# loop for inserting the array elements
for i in range(0,n):
    
    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

# displaying the array before right rotation
print('Before right rotation : ', a)

# performing shift rotation range from 0 to sr times
for i in range(0,sr):

    # stroing the last element in the temporary variable
    temp = a[n-1]

    # shifting remaining elements  toward right side.
    # the array starts with last element i.e, start with n-1  upto 0 and in reverse order -1
    for j in range(n-1, 0, -1):

        # shifting the elements
        a[j] = a[j - 1]
    
    # storing the last element to the first index 
    a[0] = temp

# displaying the array after right rotation
print('After  right rotation : ',a)