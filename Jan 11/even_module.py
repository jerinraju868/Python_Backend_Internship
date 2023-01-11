# defining a function and passing argument
def even(n,a):

    # declearing an empty array
    even = []

    # loop for taking the all values under the range 
    for i in range(n):
        
        # checking the reminder for each element if 0 then it is even number else odd
        if a[i] % 2 == 0:

            # even number is adding to another list by using the append()
            even.append(a[i])
        
    # return the even number stored array
    return even
