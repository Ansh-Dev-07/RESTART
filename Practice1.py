#find the sum of digits of a number with the help of while loop.

# num=-709
# sum=0
# while(num>0):
#     digit=num%10
#     sum+=digit
#     num//=10
# print(sum)

#using function
# def sum_of_digit(n):
#     sum=0
#     while(n>0):
#         digit=n%10
#         sum+=digit
#         n//=10
#     print(sum)
# sum_of_digit(1204)

# using for loop:
# for digit in str(num):
#     sum+=int(digit)
# print(sum)

#wap to enter a binary number and convert its decimal equivalent.
# wap to print the reverse of a number

# num=1204
# rev=0
# while(num>0):
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# print(rev)

# using function with negetive values:
# def reverse_number(n):
#     rev=0
#     sign=-1 if(n<0) else 1
#     n=abs(n)
#     while(n>0):
#         digit=n%10
#         rev=rev*10+digit
#         n//=10
#     rev=rev*sign
#     print(rev)
# reverse_number(-120)

# wap to enter a decimal number and convert its binary equivalent.
# wap to calculate the gcd of two numbers.
# a=123
# b=321
# while(b!=0):
#     a,b=b,a%b
# print(a)
# print(b)

# using function:
# def gcd(a,b):
#     while(b!=0):
#         a,b=b,a%b
#     print(a)
# gcd(12,4)

# string reverse:
# str1="hello World"
# for i in range(len(str1)-1,-1,-1):
#     print(str1[i],end="")
# print()
# print(str1[::-1])

# palindrome check:
# str2="honorificabilitudinitatibus"
# rev=""
# for i in range(len(str2)-1,-1,-1):
#     rev+=str2[i]
# if(str2==rev):
#     print("Palindrome!")
# else:
#     print("Not Palindrome!")

# rev2=str2[::-1]
# if(rev2==str2):
#     print("palindrome")
# else:
#     print("not palindrome")

# remove duplicates:
# list1=[1,2,1,3,4,5,4]
# new_list=[]
# for l in list1:
#     if(l not in new_list):
#         new_list.append(l)
# print(new_list)

# list1=list(set(list1))
# print(list1)

# print()

# frequency of words: -ignore case, -ignore punctuation
# str4="hello i am python i am very powerful language"
# s4=str4.split()
# freq={}
# for i in s4:
#     if(i in freq):
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key in freq:
#     print(key,":",freq[key])
# print()

# with function:
# def word_freq(s):
#     s1=s.lower()
#     s1=s1.split()
#     freq={}
#     for i in s1:
#         if(i not in freq):
#             freq[i]=1
#         else:
#             freq[i]+=1
#     for key in freq:
#         print(key,":",freq[key])
# word_freq("hello python , i am java . hello java , i am python , nice to meet you . nice to meet you too python .")
# print()

# character frequency
# str3="python is a powerful programming language"
# freq={}
# for i in str3:
#     if(i in freq):
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key in freq:
#     print(key,":",freq[key])
# print()

# in function
# def check_frequency(s):
#     freq={}
#     for i in s:
#         if(i in freq):
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for key in freq:
#         print(key,":",freq[key])
# check_frequency("hello my name is ansh soni")


# function on palindrome check:
# def is_palindrome(s):
#     rev=""
#     for i in range(len(s)-1,-1,-1):
#         rev+=s[i]
#     if(s==rev):
#         return True
#     else:
#         return False
# print(is_palindrome("madam"))

