''' Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
        Sample List : ['abc', 'xyz', 'aba', '1221'] 
'''

# list input 
l = ['abc', 'xyz', 'aba', '1221'] 

# declearing a variable for count
c = 0

# loop for taking each elements from the list
for i in l:

    # checking the length of the each string greater then 2 or more  and then checking for the 1st and  last elements are same 
    if len(i) > 1 and i[0] == i[-1]:

        # if the condtions become true then the counter will increase
        c += 1
    
# printing the counter value
print('No of string in the list :',c)