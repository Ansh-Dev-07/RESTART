# def vowel(s:str):
#     a="aeiou"
#     count=0
#     s=s.lower()
#     for i in s:
#         if(i in a):
#             count+=1
#     print(count)
# vowel("Hello world i am ansh")

# str1=input("Enter a string: ")
# vov_count=0
# lower=0
# upper=0
# digit=0

# for i in str1:
#     if(i.lower() in "aeiou"):
#         vov_count+=1

#     if(i.islower()):
#         lower+=1
    
#     if(i.isupper()):
#         upper+=1
    
#     if(i.isdigit()):
#         digit+=1

# print(f"Vovels Count : {vov_count}\nLower Count : {lower}\nUpper Count : {upper}\nDigit Count : {digit}")

# str1="hello"
# dict={}
# str1=str1.lower()
# for i in str1:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# for k in dict:
#     print(k,"=",dict[k])

# f=open("a.txt","r")
# content=f.read()
# print(len(content.split()))

# l=[1,2,36,4,5,36]
# print(max(l))

# s=int(input("Enter the size of list: "))
# l=[]
# for i in range(s):
#     x=int(input("Enter the element: "))
#     l.append(x)

# max=l[0]

# for i in range(len(l)):
#     if l[i] > max:
#         max=i
# print(f"index of max value: {max}")

# l1=[1,2,1,1,4,4,3,56,54,0]
# dict={}
# for i in l1:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# for k in dict:
#     print(k,"=",dict[k])

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def sum_of_digit(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum_of_digit(n-1)
# print(sum_of_digit(58))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(5))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# n=int(input("Enter the length: "))
# for i in range(n):
#     print(fibonacci(i),end=" ")

# def sum_digit(n):
#     if n==0:
#         return 0
#     else:
#         return n%10 + sum_digit(n//10)
# print(sum_digit(123))