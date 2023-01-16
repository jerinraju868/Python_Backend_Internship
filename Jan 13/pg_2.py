''' Create a text file “MyFile.txt” in python and ask the user to write separate 3 lines with three input statements from the user '''

# try block
try:

    # opeining the file using the open() function as a append mode
    file = open('Jan 13/MyFile.txt', 'a')

    # loop for adding 3 lines of inputs in a file
    for text in range(3):

        # accepting the input from the user
        text = input('Enter the text :')

        # appending the text into the file 
        file.write(text)

        # next line for each text
        file.write('\n')

# finally block for avoding the error occures
finally:

    # closing the opened file using the close()
    file.close()