#Implementing __str__ :-
# class Student:
#     def __init__(self,name,marks:list):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return self.name
#     def show(self):
#         print(f"Student name is : {self.name}\nStudent marks : {self.marks}")

# s1 = Student("Ansh Soni",[1,2,3,4,5,6])
# print(s1)
# s1.show()

# Implementing classmethods, staticmethods
# class Student:
#     school="ABC"

#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(self.name)

#     @classmethod
#     def school_name(cls):
#         print(cls.school)
    
#     @staticmethod
#     def add(a,b):
#         print(a+b)

# s1=Student("Ansh Soni")
# s1.show()
# Student.school_name()
# Student.add(2,4)

#qs on classmethod and staticmethod
# class Calculator:
#     version="1.1"

#     def multiply(self,a : int,b : int):
#         print(a*b)

#     @classmethod
#     def show_version(cls):
#         print(cls.version)
    
#     @staticmethod
#     def add(a,b):
#         print(a+b)

# c1=Calculator()
# c1.multiply(4,8)
# Calculator.show_version()
# Calculator.add(2,4)

# __str__ practice :-
# class Book:
#     def __init__(self,title:str,price:float):
#         self.title=title 
#         self.price=price
#     def __str__(self):
#         return self.title
#     def show(self):
#         print(f"The Book title is : {self.title}\nPrice : {self.price}")
# b1=Book("Python Mic on",690.46)
# print(b1)
# b1.show()

# Implemnting Overloading
# class Math:
#     def add(self,a : int,b : int,c : int = 0):
#         return a+b+c

# m=Math()
# print(m.add(2,3))
# print(m.add(2,3,4))

# __str__() example :- 
# class Student:
#     def __init__(self,name:str,marks:list):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return f"Name : {self.name} \nMarks : {self.marks}"
# s1=Student("Ansh",[1,2,3,4,5,6])
# print(s1)

# __len__() example :-
# class Student:
#     def __init__(self,marks:list):
#         self.marks=marks
    
#     def __len__(self):
#         return len(self.marks)
# s1=Student([1,2,3,4,5,6])
# print(len(s1))

# using __add__() :-
# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x + other.x
# n1=Number(5)
# n2=Number(10)
# print(n1+n2)

# using __add__() :-
# class Strings:
#     def __init__(self,x:str):
#         self.x=x
#     def __add__(self,other:str):
#         return self.x+" "+other.x
# st1=Strings("Ansh")
# st2=Strings("Soni")
# print(st1+st2)

# using __add__() :-
# class Lists:
#     def __init__(self,x:list):
#         self.x=x
#     def __add__(self,other:list):
#         return self.x + other.x
# n1=Lists([1,2,3,4,5])
# n2=Lists([6,7,8,9,0])
# print(n1+n2)