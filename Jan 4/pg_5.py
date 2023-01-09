''' Python program to replace the string space with a given character '''

# accepting the srting from user
strng =  input('Enter the string : ')

# accepting the character from user to replace the string space
ch = input('Enter the character to be replace the string space : ')

# by using the replace() funciton the string space is replaced with the character user entered
print('Replaced string : ', strng.replace(' ',ch))