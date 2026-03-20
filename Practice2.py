# sum of digits: handle negative cases.

# num=-5023
# sum=0
# num=abs(num)
# while(num>0):
#     digit=num%10
#     sum+=digit
#     num//=10
# print(sum)

#reverse a number: handle negative cases.

# num1=1005
# rev=0
# sign=-1 if(num<0) else 1
# num1=abs(num1)
# while(num1>0):
#     digit=num1%10
#     rev=rev*10+digit
#     num1//=10
# rev=rev*sign
# print(rev)

# gcd using euclidean algorithm:

# a=72
# b=30
# while(b!=0):
#     a,b=b,a%b
# print(a)

#remove duplicates while maintaining the order.

# l=[1,2,3,1,4,5,6,4,2]
# new_list=[]
# for i in l:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

#character frequency using dictionary.

# s="ansh soni is learning in python"
# s=s.lower()
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key in freq:
#     print(key,":",freq[key])
# print()

#word frequency ignoring cases.

# s="ansh soni is learning in python"
# s=s.lower()
# s=s.split()
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key in freq:
#     print(key,":",freq[key])

#armstrong number:
# num=371
# num=abs(num)
# org_num=num
# count=len(str(num))
# total=0
# while(num>0):
#     digit=num%10
#     total=total+digit**count
#     num//=10
# if(total==org_num):
#     print("Armstrong")
# else:
#     print("not armstrong")

# using function:
# def armstrong(n):
#     n=abs(n)
#     org_n=n
#     length=len(str(n))
#     sum=0
#     while(n>0):
#         digit=n%10
#         sum=sum+digit**length
#         n//=10
#     if(sum==org_n):
#         print("Armstrong")
#     else:
#         print("not armstrong")
# armstrong(100)