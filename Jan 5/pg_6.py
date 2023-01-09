''' Python Program to print all even numbers in array '''

# accepting 1st array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# declearing empty array to store the even numbers
e = []

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

# printing array
print('\nGiven Array :',a)

# for loop for taking each elements in array
for j in range(len(a)):

    # checking the each array elements for getting modulus value equal to zero
    if a[j] % 2 == 0:

        # even numbers modulus values is zero, so the zero moduls values is stored in another array
        e.append(a[j])

# displaying the array the contains only even numbers
print('Even numbers : ',e)