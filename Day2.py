#count frequency of each character in a string

#basic version - duplicate print
# str1="hello world"
# for i in str1:
#     print(i," count in ",str1," is :",str1.count(i))

#alternate version with vovels
# str1="hello beautiful"
# vovels="aeiou"
# freq={}

# str1= str1.replace(" ","")

# for i in str1:
#     if i in vovels:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
# for key in freq:
#     print(key,":",freq[key])
# print(str1)

# str1="Banana"
# freq={}

# str1=str1.lower()
# str1= str1.replace(" ","")

# for i in str1:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key in freq:
#     print(key,":",freq[key])

#for words
# str1="hello, world hello!"
# freq={}

# str1=str1.lower()
# # str1= str1.replace(" ","")
# str2=str1.split()

# for i in str2:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key in freq:
#     print(key,":",freq[key])


#remove duplicates in a list.

# list1=[1,1,34,54,233,234,34]
# print("after removing duplicate values: ",list(set(list1)))

#this is ok but what if order matters

# list1=[]

#test1
# list1=["a","A","a"]

# new_list=[]

# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

#remove duplicates ignoring cases.

# list1=["a","A","b","B"]

# list1=[i.lower() for i in list1] #list comprehension

# lower_list=[]
# for i in list1:
#     lower_list.append(i.lower())

# lower_list=list(set(lower_list))

# print(lower_list)

#test 1

# nums=[1,2,3]
# for n in nums:
#     nums.append(n)
#     print(nums)
# gives infinite loop because of appending on the same list while iterating

#test2

# nums=[1,2,3]
# for n in nums[:]:
#     nums.append(n)
#     print(nums)

# its safe and [:] creates a copy

# test3

# nums=[1,2,3,4,5]

# for n in nums:
#     if n%2==0:
#         nums.remove(n)
# print(nums)

#removing even numbers in list without list comrehension

# nums=[1,2,3,4,5,6]

# for i in range(len(nums)-1,-1,-1):
#     if nums[i] % 2 == 0:
#         nums.pop(i)
# print(nums)