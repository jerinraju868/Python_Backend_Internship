''' write a program to print the fibonacci series using recursive method '''

# defining the function
def fibonacciSeries(num):
    if num <= 1:
        return num
    else:
        return (fibonacciSeries(num - 1) + fibonacciSeries(num - 2))

# accepting the values from the user
num = int(input('Enter the limit : '))

# checking whether the user enter number is 0 or negative values
if num <= 0: 
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")

# calling the function
for i in range(num):
    print(fibonacciSeries(i), end=" ") 