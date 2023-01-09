''' Python program to reverse an Array in two ways '''

# accepting 1st array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

# before reverse the array
print('Given array is : ', a)

# reversing the array elements by using the method 'array_name[::-1]' 
print('Reverse array :', a[::-1] )