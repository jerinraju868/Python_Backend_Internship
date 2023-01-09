''' Python program to check given character is digit or not '''

# accepting the input from the user
ch = input('Enter a character : ') 

# checking the character is digit or not by using the python inbulid function isdigit()
if ch.isdigit(): 
    print('You enter digit')
else:
    print('You entered non digit')