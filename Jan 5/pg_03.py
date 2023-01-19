''' Python Program to merge two arrays '''

# accepting 1st array size
n1 = int(input('1st array size :'))

# declearing empty array
a = []

# accepting 1st array values from user
for i in range(0, n1):

    # inserting the values into an array using appern() function
   a.append(int(input("1st array value : ")))

# accepting the 2nd array size from the user
n2 = int(input('2nd array size :'))

# declearing 2nd empty array 
b = []

# accepting and storing the 2nd array values from the user
for i in range(0, n2):

    # inserting the values into an array using appern() function
   b.append(int(input("2nd array value : ")))

# merging the 2 arrays by using the + opreator
print(a+b)
