# class student:
#     ins_name="FSD"
#     def __init__(self, name,age, course):
#                 self.myName = name
#                 self.age = age
#                 self.myCourse = course
#     def display(self):
#                 print("Student Name: ", self.myName)
#                 print("Student age: ", self.age)
#                 print("Student Course: ", self.myCourse)
#                 print("Institute name: ", student.ins_name)
            
# t1=student("Abhi",20,"python")
# t1.display()

#---------------------------------------------------------------------------#

# class Bank:
#     Bank_name="Union Bank Of India"
#     Branch="Hyderabad"
    
#     def __init__(self,name,account_no,Balance,account_type):
#         self.name=name
#         self.account_no=account_no
#         self.Balance=Balance
#         self.acc_type=account_type
#     def display(self):
#         print("Customer Name : ", self.name)
#         print("Account Number : ", self.account_no)
#         print("Balance : ", self.name)
#         print("Account Type: ", self.acc_type)
#         print("Bank Name : ", Bank.Bank_name)
#         print("Branch : ", Bank.Branch)

# b=Bank("Abhishek",1234657895,5000,"Saving")
# b.display()
# print("-----------------------------------")
# b2=Bank("Bharath",4569871230,2050,"Current")
# b2.display()
# print("-----------------------------------")
# b3=Bank("Devi",2378945621,2500,"Saving")
# b3.display()
        

#---------------------------------------------------------------------------#

# class Mobile:
#     brand = "Apple"
#     country = "USA"
    
#     def __init__(self, model, price, color, storage):
#         self.model = model
#         self.price = price
#         self.color = color
#         self.storage = storage
#     def display(self):
#         print("Model:", self.model)
#         print("Price:", self.price)
#         print("Color:", self.color)
#         print("Storage:", self.storage)
#         print("Brand:", Mobile.brand)
#         print("Country:", Mobile.country)

# m=Mobile("Iphone 17",99900,"Orange","256 GB")
# m.display()

# m2=Mobile("Iphone 17 pro",150900,"Black","512 GB")
# m2.display()

# m3=Mobile("Iphone 17 pro Max",190900,"Blue","1 TB")
# m3.display()

# #---------------------------------------------------------------------------#

# class Employee:
#     company = "Tcs"
#     location = "Hyderabad"
    
#     def __init__(self, name, emp_id, salary, department):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#         self.department = department
#     def displayDetails(self):
#         print("Employee Name:", self.name)
#         print("Employee ID:", self.emp_id)
#         print("Salary:", self.salary)
#         print("Department:", self.department)
#         print("Company:", Employee.company)
#         print("Location:", Employee.location)

# E=Employee("Abhishek",1234,50000,"IT")
# E.displayDetails()
# print("------------------------------------------")
# E1=Employee("Bhai",3659,55000,"HR")
# E1.displayDetails()
# print("------------------------------------------")
# E2=Employee("Abhishek",5634,50000,"Finance")
# E2.displayDetails()
# print("------------------------------------------")
# E4 = Employee("Anil", 104, 38000, "Marketing")
# E4.displayDetails()




##---------------------destructor--------------------##
# class student:
#     def __init__(self):
#         print("Object is created : constructor is invoked")
#     def __del__(self):
#         print("Object is going to destroy : Destructor is invoked")

# s1=student()
# print("We gonna delete object --manually")

# del s1
# print("Program ended")


# class student:
#     def __init__(self):
#         print("Object is created : constructor is invoked")
#     def __del__(self):
#         print("Object is going to destroy : Destructor is invoked")

# s1=student()
# print("Program ended")


# class student:
#     institute="Innomatics"
#     @classmethod
#     def m1(cls):
#         print("Class  method",cls.institute)
    
#     @staticmethod
#     def m2():
#             print("static  method",student.institute)
        
# student.m1()
# student.m2()


# class Student:
#     institute = "Fullstack"

#     def m1(self):
#         self.name = "Hero"
#         print("Static variable ", self.institute)
#         print("Instance Variable ", self.name)

#     @classmethod
#     def m2(cls):
#         print("Static Variable ", cls.institute)
#         print("Static Variable ", cls.name)
        


