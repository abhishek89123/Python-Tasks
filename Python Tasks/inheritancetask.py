#--------------------------SINGLE INHERTANCE---------------------------- #

# Single inheritance without Constructor.

# class Teacher:
#     def teach(self):
#         print("Teacher is teaching")
# class Student(Teacher):
#     def study(self):
#         print("Student is Studying")
# s=Student()
# s.teach()
# s.study()


# Single inheritance with Constructor.

# class Student:
#     def __init__(self,name,Year):
#         self.name=name
#         self.Year=Year
#     def disaplydetails(self):
#         print("Product Name :",self.name)
#         print("Year :",self.Year)
# class Course(Student):
#     def show_course(self):
#         print("Course : Engineering")

# c=Course("Abhishek","3 rd Year")
# c.disaplydetails()
# c.show_course()


# Single inheritance with Constructor + Super()

# class Student:
#     def __init__(self,name,Year):
#         self.name=name
#         self.Year=Year
#     def disaplydetails(self):
#         print("Student Name :",self.name)
#         print("Year :",self.Year)
# class Course_details(Student):
#     def __init__(self,name,year,course,fees):
#         super().__init__(name,year)
#         self.course=course
#         self.fees=fees
#     def disaplydetails(self):
#         super().disaplydetails()
#         print("Course :",self.course)
#         print("Fees :",self.fees)
# c=Course_details("Abhi","3rd year","Engineering",75000)
# c.disaplydetails()

# Single inheritance with Constructor + Super() real world example

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        
    def display_bank(self):
        print("Bank:", self.bank_name)
        
class Account(Bank):
    def __init__(self, bank_name, account_number,Branch,IFSC_CODE):
        super().__init__(bank_name)
        self.Branch=Branch
        self.account_number = account_number
        self.ifsc_code=IFSC_CODE
        
    def display_account(self):
        super().display_bank()
        print("Branch :", self.Branch)
        print("Account Number:", self.account_number)
        print("IFSC CODE:", self.ifsc_code)
        
a = Account("SBI", "79865451","Hyderabad","SBIN84861000")
a.display_account()






#--------------------------MULTILEVEL INHERTANCE------------------------- #


# Multilevel inheritance without Constructor.

# class Grandfather:
#     def property(self):
#         print("Grand father has property")

# class Father(Grandfather):
#     def car(self):
#         print("Father has car")
        
# class Child(Father):
#     def bike(self):
#         print("Son has bike")
        
# c=Child()
# c.property()
# c.car()
# c.bike()



# Multilevel inheritance with Constructor.

# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def display_name(self):
#         print("Name:", self.name)

# class Student(Person):
#     def __init__(self, name, course):
#         Person.__init__(self, name)
#         self.course = course

#     def display_course(self):
#         print("Course:", self.course)

# class CollegeStudent(Student):
#     def __init__(self, name, course, college):
#         Student.__init__(self, name, course)
#         self.college = college

#     def display_college(self):
#         print("College:", self.college)

# s = CollegeStudent("Abhishek", "Python", "Sphoorthy Engineering College")

# s.display_name()
# s.display_course()
# s.display_college()





# Multilevel inheritance with Constructor + super().


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print("Animal:", self.name)

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def display_breed(self):
#         print("Breed:", self.breed)

# class Puppy(Dog):
#     def __init__(self, name, breed, age):
#         super().__init__(name, breed)
#         self.age = age

#     def display_age(self):
#         super().display_name()
#         super().display_breed()
#         print("Age:", self.age)

# p = Puppy("Tommy", "Labrador", 2)
# p.display_age()




# Multilevel inheritance with Constructor + Super() real world example.


class Employee:
    def __init__(self, name):
        self.name = name
    def display_employee(self):
        print("Employee Name:", self.name)

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
    def display_language(self):
        print("Programming Language:", self.language)
        
class SeniorDeveloper(Developer):
    def __init__(self, name, language, experience,salary):
        super().__init__(name, language)
        self.experience = experience
        self.salary=salary
    def display_experience(self):
        super().display_employee()
        super().display_language()
        print("Experience:", self.experience, "years")
        print("Salary :",self.salary)

d = SeniorDeveloper("Rahul", "Python", 5,65000)

d.display_experience()