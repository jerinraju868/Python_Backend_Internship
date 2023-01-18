''' 
Create a class Employee with name and id, salary attributes.
The salary has to be calculated and should be initialized to zero.
Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You can give no of hours to the method as an argument.
Now create a child class ParttimeEmployee by inheriting the Employee class, and by using method overriding (create salary calculation method in this class also with the same)
print the salary of part time employee by multiplyig no of hours worked by 150.
Also implement '+' operator overloading using __add__ to find the total expense of paying salaries to employees(Find the total salary of all the created employees and  parttime employees)
'''

# Parent class called Employee
class Employee:

    # constructor with name, id, hrs  as instance variables
    def __init__(self,name,id, hrs):

        # declearing instance variable name
        self.name=name

        # declearing instance variable id
        self.id=id
        
        # declearing instance variable hrs
        self.hrs = hrs

        # declearing instance variable salary as initial value as zero
        self.salary = 0
    
    # defining instance method  called  calculatesalary()
    def calculatesalary(self):

        # printing the employee details
        print(f'\nID : {self.id} | Name : {self.name}  | Working hours : {self.hrs}')

        # calculating the salary by multiplying no. of working hrs with 200
        self.salary = self.hrs * 200

        # displaying the salary
        print('Permenent Salary : ', self.salary)
    
    # defining operator overloading using __add__() function by accepting the list as input to find the total expense for the each user
    def __add__(list):

        # initilising the total variable as zero
        total = 0

        # loop for taking the each permenent employees salaries 
        for i in list:

            # adding the each employee salary and add it with total
            total += i.salary

        # return the total
        return total

# Child class named ParttimeEmployee
class ParttimeEmployee(Employee):

    # defining instance method 
    def calculatesalary(self):

        # printing the employee details
        print(f'\nID : {self.id} | Name : {self.name} | Working hours : {self.hrs}')

        # calculating the salary for part time employee by multiplying no. of working hrs with 150
        self.salary = self.hrs * 150

        # displaying the part time salary
        print('PartTme Salary : ', self.salary)

    # defining operator overloading using __add__() function by accepting the list as input to find the total expense for the each user
    def __add__(list):

        # initilising the total variable as zero
        total = 0

        # loop for taking the each permenent employees salaries 
        for i in list:

            # adding the each employee salary and add it with total
            total += i.salary

        # return the total
        return total

# declearing the object for the child class by passing the arguments as name , id and working hours
emp1 = Employee('jerin', '001', 10)
emp2 = ParttimeEmployee('Sherin', '002', 10)
emp3 = Employee('Merin', '003', 10)
emp4 = ParttimeEmployee('Molly', '004', 10)

# calling the child class method using the object created above 
emp1.calculatesalary()
emp2.calculatesalary()
emp3.calculatesalary()
emp4.calculatesalary()

# calling the parent class __add__() function by passing the the all employees as list to calculate the permanent employee total salary and stores in t1
t1 = Employee.__add__({emp1, emp3})

# calling the parent class __add__() function by passing the the all employees as list to calculate the part time employee total salary and stores in t2
t2 = ParttimeEmployee.__add__({emp2, emp4})

# displaying the total expense by adding the total of permanent and part time employees
print('\nTotal Expense :', t1 + t2)