''' 
Write a Python script to merge the following dictionaries to create a new one. 
    Sample Dictionary : dict1={1:10, 2:20}
                        dict2={3:30, 4:40}
                        dict3={5:50, 6:60}
    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

# declearing 1st dictionary
dict1 = {1:10, 2:20}

# declearing 2nd dictionary
dict2 = {3:30, 4:40}

# declearing 3rd dictionary
dict3 = {5:50, 6:60}

# new dictionary to store the merged above dictionaries
dict4 = {**dict1, **dict2, **dict3} 

# printing the merged dictionary
print('After Merging :', dict4)