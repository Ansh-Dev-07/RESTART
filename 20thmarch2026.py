# File handling:-
# f = open("a.txt","w")
# f.write("Enter your full name: ")
# f.close()

# f = open("a.txt","a")
# name=input("Enter your full name: ")
# f.write(name)
# f.close()

# f = open("a.txt","r")
# content=f.read()
# print(content)
# f.close()

# OOPs basic concept:-
# class Student:
#     def __init__(self,name,roll,marks : list):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def display(self):
#         print(f"The Name of student is : {self.name}\nand his Roll no. is : {self.roll}\nand his marks are : {self.marks}")

# obj1=Student("Ansh Soni",19,[55,48,47,29,58])
# obj2=Student("Rahul Kushwaha",33,[67,63,58,34,65])
# obj1.display()
# obj2.display()

# Exception Handling:-
# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))

#     result=a/b

#     print(result)
# except Exception as e:
#     print(e)

# except ZeroDivisionError as z:
#     print(z)

# else:
#     print("Working straignt nigga!")

# finally:
#     print("Thank you for using us!")

# Created user-defined Exception:-
# class Myerror(Exception):
#     pass

# try:
#     age=int(input("Enter your age: "))

#     if age<0 or age>100:
#         raise Myerror("invalid Age!")
#     else:
#         print(age)
    
# except Myerror as m:
#     print("My own error: ",m)

# Implementing Encapsulation
# class Bank_Account:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def withdraw(self,amount: int):
#         if(amount > self.__balance):
#             print("Insufficient balance!")
#         else:
#             self.__balance=self.__balance - amount
#             print("Withdrawn successfully!")
#     def deposit(self,amount: int):
#         self.__balance += amount
#         print("Amount added to your Account!")
#     def display(self):
#         print(f"Your current balance is : {self.__balance}")
# obj1=Bank_Account("Ansh Soni",400)
# obj1.deposit(1500)
# obj1.withdraw(500)
# obj1.display()

# Implementing Inheritance
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"Person's Name : {self.name}\nPerson's age : {self.age}")

# class Student(Person):
#     def __init__(self,name,age,marks : list):
#         super().__init__(name, age)
#         self.marks=marks
#     def show_marks(self):
#         print(f"The marks are : {self.marks}")

# obj1=Student("Ansh",21,[58,55,52,34,60])
# obj1.show()
# obj1.show_marks()

# Implementing Polymorphism
# class Animal:
#     def sound(self):
#         print("Random animal noises...")

# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks...")

# class Cat(Animal):
#     def sound(self):
#         print("Cat Meows...")

# d1=Dog()
# c1=Cat()
# d1.sound()
# c1.sound()

