''' Write a Python code to remove all characters except a specified character in a given string
        Sample String : 'exercises'
        ExpectedResult : 'eee' (Removed  all characters except special character : e)
'''

# accepting the string from the user
strng = input('Enter the string : ')

# accepting the character
ch = input('Enter the special character : ')

# initializing an array 
a = []

# loop for taking each character
for i in range(len(strng)):

    # checking the each character for same as the user entered character
    if strng[i] == ch:

        # the character is stored in another array using the append()
        a.append(strng[i])
    
# printing the array elemente usig join() function
print(''.join(a))