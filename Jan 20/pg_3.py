''' 
Python Sequences:
    Write a program that takes in a list of strings and returns a new list with all the strings in uppercase
'''

# accepting the list size from the user
n = int(input('How many elements in the list : '))

# initilizing the empty list1 for accepting the list items from the user
list1 = []

# initilizing the empty list2 for storing the uppercase elements of the list1
list2 = []

# loop for accepting the list item from the user
for i in range(n):

    # accepting the list items from the user and stores in list1 by using the append() function
    list1.append(input('Enter the list element : '))

# displaying the list before converting the elements into uppercase
print('\nYour list :', list1)

# loop for converting the each elements of the list1 to uppercase and stores in another list2
for j in list1:

    # converting the list1 elements to uppercae and stores in list2 by using the upper() function
    list2.append(j.upper())

# displaying the list2 elements
print('\nNew list :',list2)