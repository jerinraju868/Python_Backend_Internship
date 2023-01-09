''' Write a python program to find the sum of all items in a dictionary
    
            Input : {'a': 100, 'b':200, 'c':300}
'''

# declearing the dictonary
dict = {'a': 100, 'b':200, 'c':300}

# declearing a variable to store the sum
sum = 0

# loop for taking each element in the dictonary
for i in dict:

    # taking each digit from dictonary and adding 
    sum += dict[i]

# displaying the sum
print('Sum :' ,sum)
