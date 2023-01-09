''' write a python program to find the difference between two lists
        list1 = [10, 15, 20, 25, 30, 35, 40]
        list2 = [25, 40, 35] 
 '''

# inputs
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 

# empty list to store the different list elements
list3 = []

# loop for taking the each elements in list
for i in list1:

    # comparing with the list1 element with list2 elements, if there is no same elements is present then they store in another list3
    if i not in list2:

        # adding the non commmon element in the list3
        list3.append(i)
        
print('List 1 :',list1)
print('List 2 :',list2)

# displaying the differenc between the list1 and list2
print('Difference is :',list3)