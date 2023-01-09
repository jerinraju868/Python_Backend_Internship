''' python program to delete vowels in a given string '''

# taking input from the user
string = input('Enter the string : ')

# declearing a list contains all vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# declear a new variable
result = "" 

for i in range(len(string)):
    
    # taking each character and checking for the vowels 
    if string[i] not in vowels: 
        
        # only the non vowels character is stored in result and creating new list called result
        result = result + string[i] 

# printing the list 'result'
print("\nAfter removing Vowels:", result)