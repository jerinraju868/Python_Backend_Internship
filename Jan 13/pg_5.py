''' Read the contents of intro.txt file in reverse order '''

# opening intro.txt as a file in read mode
with open('Jan 13/intro.txt', 'r') as file:

    # reading the file and stores in a variable called data
    data = file.read()

# reversing the data and stores in variable called rev
rev = data[::-1]

# displaying the reverse data that is stored in rev variable
print('Reverse order\n', rev)