'''
Python File handling:
    Create a program that reads a text file and prints the number of lines in it
'''

# opeining the file in read mode
f = open('Jan 20/Activity.txt', 'r')

# reading the file using the readlines() funtion and convert into list
lines = f.readlines()

# calculating the length of the list 
length = len(lines)

# printing the length
print('No. of lines : ',length)


# closing the file
f.close()