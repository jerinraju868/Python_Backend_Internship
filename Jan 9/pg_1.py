''' Write a Python program to remove duplicates from a list '''

# accepting the list size from the user
n = int(input('Enter the size of list :'))

# declearing the empyt list to store the list elements 
l = []

# loop for accepting the list elements from the user and stores in l
for i in range(0,n):

    # adding the list elements from user and stores in l by using the append() function
    l.append(int(input("Enter list value : ")))

# before remving the duplicate item from the list
print('Before removing the duplicate elements : ',list(l))

# converting the list into set()
res = list(set(l))

# displaying the result
print('After  removing the duplicate elements : ', res)
