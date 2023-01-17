'''
Read an input name from the user and loop through the below list of dictionaries and find the dictionaries that has a matching name which the user has entered.
    For eg: If the user enters 'John', then both the dictionaries that matches 'John' and 'John Doe' needs to be displayed.
    
            data = [{"name": "John","age": 30,},
                    {"name": "David","age": 28,},
                    {"name": "Miller","age": 29,},
                    {"name": "David Miller","age": 32,},
                    {"name": "John Doe","age": 30,},
            ]

'''

# input list of dictionary
data = [
            {"name": "John","age": 30,},
            {"name": "David","age": 28,},
            {"name": "Miller","age": 29,},
            {"name": "David Miller","age": 32,},
            {"name": "John Doe","age": 30,},
        ]
# accepting  the input name from the user
name = input("enter the name of the person:")

# loop for taking the each element in the list
for i in data:

    # checking the each element with user inputed name
    if  name in i["name"]:

        # displaying the data  
        print(i)
    
# for loop else for printing the error message
else:

    # error message
    print('No record found...!')
