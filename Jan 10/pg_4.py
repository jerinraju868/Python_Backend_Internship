''' Python program to check the score from a student 
    print grades as 
        A+ if score >= 90,
        A if 80 or above, 
        B+ if 70 or above and so on...  
        print failed if the score is below 50, 
        if score > 100 print invalid 
'''

# accepting the score from user
score = int(input('Enter your score : '))

# conditions
if score > 100:
    print('Invalid ')
elif score >= 90:
    print('Grade : A+')
elif score >= 80:
    print('Grade : A')
elif score >= 70:
    print('Grade : B+')
elif score >= 60:
    print('Grade : B')
elif score >= 50:
    print('Grade : C+')
else:
    print('Failed..!')




