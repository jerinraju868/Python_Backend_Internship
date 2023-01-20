'''
Python Functions:
    Create a function that takes in a string and returns the number of vowels in it
'''

# creating a function called count_vowels 
def count_vowels(strng):

    # declearing list of vowels
    vowels = ['a','e','i','o','u']

    # initialize counter variable  as zero
    count = 0

    # loop for taking the each letters from the string
    for letter in strng:

        # checking the each letter with the each elements in list of vowels. if found, then the counter variable increased
        if letter in vowels:

            # counter variable increased by 1
            count += 1
    
    # returning the counter variable
    return count

# accepting the  input string from the user
strng = input('Enter the string : ')

# calling the count_vowels() by passing the string that is converted to lowercase using lower() function
obj = count_vowels(strng.lower())

# printing the result 
print('No of vowels :',obj)