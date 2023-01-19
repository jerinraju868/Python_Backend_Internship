''' Python program to print the highest frequency character in a String '''

from collections import Counter

# accepting the string from the user
strng = input('Enter the string : ')

# by using the counter() function calculating the count of the each character 
count = Counter(strng)

# by using the max() function the highest counted character is stored in the result
result = max(count, key=count.get)

# printing the result
print("Highest frequency character : ",result)
