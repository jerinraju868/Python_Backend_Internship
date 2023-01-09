''' Python Program to calculate length of an array '''

# accepting 1st array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

# calculating the length of the array using len() function
print('Length of the given array :', len(a))