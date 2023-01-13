''' Append the contents in entered by the user in the intro.txt file '''

# opening intro.txt as a file in append mode
with open('Jan 13/intro.txt', 'a') as file:

    # accepting the data from the user and stores in the variable called data 
    data = input('Enter the data : ')

    # for next line
    file.write('\n')

    # appending the data into the file intro.txt
    file.write(data)