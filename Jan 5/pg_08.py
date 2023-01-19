''' Python Program to delete element from array at given index '''

# accepting 1st array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

print('Array :', a)

# accepting the index value to delete the particular item from particular index
x = int(input('Enter the index No. to delete element : '))

# for taking each element
for j in range(len(a)):

    # checking the each index is same as the user given index, if same, the item remove
    if x == j:
        a.remove(a[j])

# displaying the array after removing particular index value fronm array
print('After removing the item :',a)
