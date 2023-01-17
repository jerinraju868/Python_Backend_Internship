''' Write a Python class named Student with school_name as class variable, and name, id as instance variables. 
    And create two objects student_1, student_2 Assign name and id values to the objects using constructor. 
    Print all the attributes of student1, student2 objects by using another instance method called display_student
'''

# declearing the class called Stundent
class Student:

    # class variable called school_name
    school_name = 'A P J Abdul Kalam Technological University'

    # constructor with name, id  as instance variables 
    def __init__(self, name, id):

        # instance varible name
        self.name = name

        # instance variable id
        self.id = id

    # defining instance method 
    def display_student(self):

        # printing the student details
        print('ID: ', self.id,'| Name: ', self.name )

# declearing a objecct for the student1 by  passing the arguments name and id number 
student1 = Student('Jerin', '0001')

# declearing a object for the student2 by passing the arguments name and id number 
student2 = Student('Sherin', '0002')
    
# calling the instance method for the student1
student1.display_student()

# calling the instance method for the student2
student2.display_student()
