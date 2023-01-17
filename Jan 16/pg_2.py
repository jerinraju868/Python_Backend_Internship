'''
Write a Python program to calculate the product of the unique numbers of a given list
    Original List : [10, 20, 30, 40, 20, 50, 60, 40]
    Product of the unique numbers of the said list: 720000000
'''

# initilising the list
list1 = [10, 20, 30, 40, 20, 50, 60, 40]

# coverting the list to set to avoid the duplicated/repeated elements from the list and stored in another list
list2 = set(list1)


# initilizing a variable called product to store the product of each elements
product = 1

# loop for taking the each elements from the list2
for i in list2:

    # multiply the each elements with the previous products
    product *= i

# printing the final result 
print("Product :",product)