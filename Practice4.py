# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def increase_salary(self):
#         self.salary=self.salary+self.salary*10/100
#     def show_details(self):
#         print(f"Employee Name: {self.name}\nEmployee salary: {self.salary}")
# e1=Employee("Ansh",64000)
# e1.increase_salary()
# e1.show_details()

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         print("your current bank balance is: ",self.balance)
#         print("You want to deposit ",amount," amount.")
#         self.balance=self.balance+amount
#         print("your current bank balance is: ",self.balance)
#     def withdraw(self,amount):
#         print("your current bank balance is: ",self.balance)
#         print("You want to withdraw ",amount," amount.")
#         if(amount>self.balance):
#             print("Insufficient Balance!")
#         else:
#             self.balance=self.balance-amount
#     def display(self):
#         print("Account holder name: ",self.name)
#         print("Account current balance: ",self.balance)
# bk1=BankAccount("ANSH SONI",100)
# bk1.display()
# bk1.deposit(1000)
# bk1.display()
# bk1.withdraw(7000)
# bk1.display()

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         area=self.length*self.width
#         print(area)
#     def perimeter(self):
#         perimeter=2*(self.length+self.width)
#         print(perimeter)
# rect1=Rectangle(34,54)
# rect1.perimeter()
# rect1.area()

