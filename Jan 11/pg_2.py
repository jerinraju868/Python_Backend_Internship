''' Write a function to find the largest item from a given list '''

# accepting the list size from the user
n =  int(input('Enter the list size : '))

# declearing an empty array
a = []

# loop for accepting and storing the list elements
for i in range(n):

    # adding the elements to array
    a.append(int(input("Enter value : ")))

# displaying the largest number from the list by using the max() function
print('Largest number in an array : ', max(a))