''' Python Program to print all odd numbers in array '''

# accepting 1st array size
n = int(input('Enter array size :'))

# declearing empty array to store array elements
a = []

# declearing empty array to store the odd elements
o = []

# accepting array values from user
for i in range(0, n):

    # inserting the values into an array using appern() function
    a.append(int(input("Enter array value : ")))

# printing array
print('\nGiven Array :',a)

# for loop for taking each elements in array
for j in range(len(a)):

    # checking the array each array elements for getting modulus value not equal to zero
    if a[j] % 2 != 0:

        # odd numbers modulus values in non zero elements so the non zero modulus elements is stored in another array
        o.append(a[j])

# displaying the array the contains only odd numbers
print('Odd numbers : ',o)