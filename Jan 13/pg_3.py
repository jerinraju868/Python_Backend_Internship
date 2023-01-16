''' Write a program to read the contents of both the files created in the above programs and merge the contents into “merge.txt”.
   Avoid using the close() function to close the files ? 
'''

# opening the intro.txt as file1 in read mode
with open('Jan 13/intro.txt', 'r') as file1:

    # reading the each text in the file1 using the read() and stores in variable called data1
    data1 = file1.read()

# opening the MyFile.txt as file2 in read mode
with open('Jan 13/MyFile.txt', 'r') as file2:

    # reading the each text in the file2 using the read() function and stores in variable called data2
    data2 = file2.read()

# opening merge.txt as a file3 in write mode
with open('Jan 13/merge.txt', 'w') as file3:

    # adding the data1 to the file3
    file3.write(data1)

    # next line
    file3.write('\n')

    # adding the data2 into the file3
    file3.write(data2)
    

