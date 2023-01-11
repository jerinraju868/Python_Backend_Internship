''' 
    Write a Python function that takes a list and returns a new list with unique elements of the first list
        Sample List : [1,2,3,3,3,3,4,5]
        Unique List : [1, 2, 3, 4, 5]
'''
# accepting the list size from the user
n =  int(input('Enter the list size : '))

# declearing an empty array
a = []

# loop for accepting and storing the list elements
for i in range(n):

    # adding the elements to array
    a.append(int(input("Enter value : ")))

# displaying the list before deleting the duplicate elements
print('Entered list : ', a)

# displaying the largest number from the list by using the max() function
print('New List : ', list(set(a)))