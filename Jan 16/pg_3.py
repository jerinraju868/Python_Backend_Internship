'''
Write a program to create a list like this
    [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
'''

# initilizing the empty list
l = []

# adding elemnets into the list under the range 1 to 11 
for i in range(1,11):

    # adding the elements into the list using the append() function
    l.append(i)

# loop for adding the list elements in reverse order under the range and condition 9 to 0 with -1 decrement
for j in range(9,0,-1):

    # adding the elements into the list using the append() function
    l.append(j)

# displaying the list
print(l)