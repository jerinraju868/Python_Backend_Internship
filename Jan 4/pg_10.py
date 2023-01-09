''' Write a program in Python to find largest and smallest number in array '''

# accepting the input for the size of an array 
size = int(input("enter the lentgh of array : "))

# declearing an empty array
arr = []

# for loop for accepting the array element from the user
for i in range(size):

    # by using append() function, the elements are added into the array
    arr.append(int(input("Enter the Values : ")))

#  printing the smallest number in the array by using min() function
print("\nSmallest number is :",min(arr))

#  printing the laegest number in the array by using max() function
print("Largest number is :",max(arr))