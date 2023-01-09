''' write a python program to capitalize the first and last character of each word in a string '''

# accepting the input string from the user
s = input('Enter the string : ')

# spliting the string using split() function
a = s.split()

# declearing the empty array to store the character after the operation performed
res = []

# taking each elements from the list
for i in a:

    # converting the 1st and last elements to upper case using the upper() function
    x = i[0].upper()+i[1:-1]+i[-1].upper()

    # appending the changed elements to res
    res.append(x)

    # join operation performed
    res = " ".join(res)

# displaying the changed string
print("String after:", res)

    