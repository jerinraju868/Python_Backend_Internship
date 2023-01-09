''' write a python program to reverse words in a given String in Python 
        Input : str = my name is laxmi
        output : str= laxmi is name my 
'''

# input string
String = 'my name is laxmi'


# before the reverse words
print('Before the reverse words :', String)
# reversing words in a given string
s = String.split()[::-1]

# declearing a new array to store the words
l = []

# loop for taking the each word from the string
for i in s:

    # apending reversed words to l
    l.append(i)

# printing reverse words
print('After  the reverse words :', " ".join(l))
