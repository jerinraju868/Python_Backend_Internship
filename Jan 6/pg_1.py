''' Write a program for printing pyramid patterns in python
* 
* * 
* * * 
* * * * 
* * * * * 
'''

# for loop for each row 
for i in range(1,6):

    # loop for printing the * in each columns 
    for j in range(i):

        # printing the * and space betweeen each *
        print('*', end= ' ')

    # next line for next row
    print('\n')