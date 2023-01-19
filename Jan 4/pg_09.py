''' Python Program to sort characters of string in ascending order '''

# accepting the input fro the user
strng = input('Enter the string : ')

# by using the sorted() function the string elements are sorting
sort = sorted(strng)

# after sorting, the each elements are combined together 
result = ''.join(sort)

# print the sorted character in string
print(result)
