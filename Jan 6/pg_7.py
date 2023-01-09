''' write a python program to interchange first and last elements in a list 
    Input : [1, 2, 3]
    Output : [3, 2, 1]
'''

# input
list1 = [1,2,3]

# before interchang the list1 is displaying
print('Befor interchanging : ',list1)

# swapping the first and last elements
list1[0], list1[-1] = list1[-1], list1[0]

# after interchanging the elements, display the list
print('After interchanging :',list1)