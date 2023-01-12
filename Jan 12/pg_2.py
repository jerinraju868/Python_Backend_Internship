''' Print even length words in a string.
    Sample String : ''I love  coding"
    ExpectedResult : “love, coding”
'''

# accepting the input string from the user
strng = input('Enter the string : ')

# spliting the string from space
seperate = strng.split(' ')

# declearing a empty array for stroing the even lengthed string 
a = []

#  loop for each word in string
for word in seperate:

    # checking for the word length is even
    if len(word) % 2  == 0:

        # adding the word to another array 
        a.append(word)

# displaying the array with even length words
print(', '.join(a))

     