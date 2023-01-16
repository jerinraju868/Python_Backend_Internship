'''
Write a Python program to find the key that has the highest value in a dictionary.
    {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
'''

# declearing the dictionary 
dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

# finding the highest values from the dictionary using the max() function
max = max(dict1.values())

# printing the highest values
print('Highest value :', max)