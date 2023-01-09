''' Write a Python program to convert list to list of dictionaries
    Sample lists:   ["Black", "Red", "Maroon", "Yellow"]
                    ["#000000", "#FF0000", "#800000", "#FFFF00"]
    Expected Output: [
                        {'color_name': 'Black', 'color_code': '#000000'}, 
                        {'color_name': 'Red', 'color_code': '#FF0000'}, 
                        {'color_name': 'Maroon', 'color_code': '#800000'}, 
                        {'color_name': 'Yellow', 'color_code': '#FFFF00'}
                    ]
'''

# declearing the list1 with values of color name
list1 = ["Black", "Red", "Maroon", "Yellow"]

# declearing the list2 with calues of color code
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# using zip() function, list1 and list2 are combined together
for name, code in zip(list1, list2):

    # printing the list1 and list2 combined and converted to dictonary
    print([{'color_name':name,'color_code':code}])

