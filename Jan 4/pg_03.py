''' Python program to remove given character from String '''

# accepting string from the user
strng = input('Enter the string : ') 

# accepting the character from the user
char = input('Enter the character to remove : ') 

# declearing variable
result = '' 

for i in range(len(strng)):
    
    # checking whether the string contains the user entered character, if it the ignores 
    if strng[i] != char : 
        
        # creating new string by removing the user enter character
        result += strng[i] 

# printing the result
print(result) 
