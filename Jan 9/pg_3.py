''' Write a python program to sort dictionary by values (Ascending/ Descending) '''

# input dictonary
dict1 = {1:'one', 3:'three',4:'four', 2:'two'} 

# before sorting the dictonary
print('Before sorting :', dict1)  
                                         
# convet the given dictondary into list. items() method is used to return the list
l = list(dict1.items())  

# sorting the list
l.sort()            

# converting the list into dictonary
dict2 = dict(l)

# print the sorted list as ascending order 
print('Ascending order is',dict2)


#sorting  in reverse order
l.sort(reverse=True) 

# converting the list into dictonary
dict3 = dict(l)

# print the sorted list as decending order 
print('Descending order is',dict3)