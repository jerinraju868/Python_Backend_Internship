'''
Python Strings:
    Write a program that takes in a string and returns the number of times a specific word appears in it
'''

# accepting the  string from the user and spliting the string with blankspace using the split() function
strng = input('Enter the string : ').split(' ')

# accepting the word from the user
word = input('Enter the  word : ')

# counter variable
count = 0

# loop for taking the each word from the string  
for i in strng:
        
    # checking the word with the current word from the string. if it matches , counter increases
    if (word == i):

        # counter increases by 1
        count += 1

# printing the count
print(f'\nThe `{word}` is occurs in `{count}` times\n')
