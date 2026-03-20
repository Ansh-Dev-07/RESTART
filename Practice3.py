#fibonacci

# num=10
# a,b=0,1
# for i in range(num):
#     print(a,end=" ")
#     a,b=b,a+b
# print()

# fibonacci using function

# def fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# num=int(input("Enter a number: "))
# fibonacci(num)

# second largest in list:

# list1=[1,2,11,54,232,434,31]
# largest=list1[0]
# second_largest=None
# for l in list1:
#     if(l>largest):
#         second_largest=largest
#         largest=l
#     elif(l!=largest and (second_largest is None or l>second_largest)):
#         second_largest=l
# print(largest)
# print(second_largest)

# second largest in list using function:

# def sec_large_in_list(l1):
#     large=l1[0]
#     second_large=None
#     for l in l1:
#         if(l>large):
#             second_large=large
#             large=l
#         elif(l!=large and (second_large is None or l>second_large)):
#             second_large=l
#     print(large)
#     print(second_large)
# size=int(input("Enter the number of element you want in lists: "))
# list1=[]
# for i in range(size):
#     num=int(input("Enter number: "))
#     list1.append(num)
# print(list1)
# sec_large_in_list(list1)

# student above average:

# marks={"A":94,"B":94,"C":78,"D":65}
# avg=sum(marks.values())/len(marks)
# print("The average is: ",avg)
# for name,mark in marks.items():
#     if(mark>avg):
#         print(name)

# student with max marks:

# marks={"A":94,"B":94,"C":78,"D":65}
# max_marks=max(marks.values())
# for name,mark in marks.items():
#     if(mark==max_marks):
#         print(name)

# salary employees:
# employees={"Aman":30000,"Shanti":45000,"Ali":25000,"Dev":50000}
# #increase salary:
# for name,salary in employees.items():
#     if(salary < 39000):
#         employees[name]=salary * 1.1
# print(employees)
# #decrease salary:
# for name,salary in employees.items():
#     if(salary > 39000):
#         employees[name]=salary-(salary*0.1)
# print(employees)

#prime number using function:
# def is_prime(n):
#     if(n<=1):
#         print("Not prime!")
#         return
#     for i in range(2,n):
#         if(n%i!=0):
#             print("Prime")
#             return
#     print("Not Prime!")
# is_prime(29)