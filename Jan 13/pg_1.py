''' Create a text file “intro.txt” in python and ask the user to write a single line of text by user input '''

# try block
try:

    # file is opening with open() method as a write mode 
    file = open('Jan 13/intro.txt','w')

    # accepting the single line input text from the user
    text = input('Enter the single line text : ')
    
    #  writing the text into the file using the write() mehthod
    file.write(text)

# finally block to avoid errors
finally:

    # closing the file using close() function
    file.close()