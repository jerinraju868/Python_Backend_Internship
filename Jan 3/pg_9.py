''' check the given number is prime or not '''

num = int(input('enter the number: ')) # getting input from the user

if num < 1 : 
    print('not a prime number')

else:
    for i in range(2, num):
        if num % i == 0:
            print(num, 'is not prime')
            break
    else:
        print(num, 'is prime number')