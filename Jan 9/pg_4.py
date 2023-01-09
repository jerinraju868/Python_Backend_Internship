''' Write a Python program to print the numbers of a specified list after removing even numbers from it.(use list comprehension)
    list = [7,8, 120, 25, 44, 20, 27]
'''

# list input
l = [7,8, 120, 25, 44, 20, 27]

# declearing an empty array
a = []

# displaying the list before removing the even numbers
print('Before removing the even numbers : ', l)

# loop for taking each elements from list
for i in range(len(l)):

    # checking the each element and dividing with 2 and if the remainder is non zero number then it is an odd number so it is stored in another array
    if l[i] % 2 != 0:

        # adding the elements to array by using the append() function
        a.append(l[i])
    
# displaying the array with only containes the no even numbers
print('After Removing the even numbers :',a)