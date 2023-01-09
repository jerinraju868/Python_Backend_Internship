''' find the reverse of a given number '''

num = int(input('enter the number: '))

def rev(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = (rev * 10 ) + rem
        num = num // 10
    return rev

print('reverse of ',num, 'is',rev(num))