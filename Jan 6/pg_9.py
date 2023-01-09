''' write a python program to print to print half Diamond star pattern	 '''

# half diamond size input reciving from the user 
n = int(input('Enter the limit :'))

# loop for printing upper stars
for i in range(n):
    for j in range(0, i+1):
        print('*', end= '')
    print()

# loop for printing the lower stars
for i in range(1, n):
    for j in range(i, n):
        print('*', end='')
    print()