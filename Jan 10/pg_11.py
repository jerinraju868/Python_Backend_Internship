''' Print first 10 fibonacci numbers using 'for' and 'while' loops '''

# initilizing the limit
n = 10

# initilizing the 1st element
a = 0                        

# initilizing the 2nd element
b = 1

# checking the number is greater/ less then the 0                              
if n <= 0:
    print("The requested series is",n)
else:

    # priinting the 1st and 2nd elements
    print(a,b,end=" ")

    # loop for printing the remaining elements 2 to n range
    for i in range(2,n):

        # adding the each elements
        x = a + b    

        # printing the sum                      
        print(x ,end=" ")

        # shifting the elements
        a, b = b,x
    
    # nextline
    print()