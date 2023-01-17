''' Extend the above program and add a score variable as an instance variable. 
    Create a static method named average_score.
    And call the method with list of created objects to find the average score ?
'''

# declearing the class called Stundent
class Student:

    # class variable called school_name
    school_name = 'A P J Abdul Kalam Technological University'
    
     # constructor with name, id, score  as instance variables
    def __init__(self, name, id, score):
        
        # instance varible name
        self.name = name

        # instance variable id
        self.id = id
        
        # instance variable score
        self.score = score

    # defining instance method 
    def display_student(self):

        # printing the student details
        print('ID: ', self.id,'| Name: ', self.name)

    # declearing the static method called average_score by passing the list as argument using the @staticmethod decorator
    @staticmethod
    def average_score(list):

        # declearing a variable c as 0
        c = 0

        # loop for taking the  each element in the list
        for i in list:

            # adding the each student scores and stores in c
            c += i.score
        
        # calculating the average 
        avg = c / len(list)

        # return the average
        return  avg

# declearing a objecct for the student1 by  passing the arguments name and id number 
student1 = Student('Jerin', '0001',250)

# declearing a object for the student2 by passing the arguments name and id number 
student2 = Student('Sherin', '0002',50)

# calling the instance method for the student1  
student1.display_student()

# calling the instance method for the student2
student2.display_student()

# declearing the object for calling the static method decleared in the class Student by passing the arguments as list
avg = Student.average_score({student1, student2})

# printing the average
print('Total Average : ', avg)