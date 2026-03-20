# s1=input("Enter a string: ")
# upper_count=0
# lower_count=0
# digit_count=0
# for i in s1:
#     if(i.isupper()):
#         upper_count+=1
#     elif(i.islower()):
#         lower_count+=1
#     elif(i.isdigit()):
#         digit_count+=1
#     else:
#         print("invalid!")
# print(f"Upper = {upper_count} \nLower = {lower_count} \nDigit = {digit_count}")

# str1="madam"
# str2=""
# for i in range(len(str1)-1,-1,-1):
#     str2=str2+str1[i]
# if str1 == str2:
#     print("Palindrome!")
# else:
#     print("Not palindrome!")

# vovels="aeiou"
# vovels_count=0
# consonent_count=0
# s1=input("Enter a string: ")
# s1=s1.lower()
# # print(s1)
# for i in s1:
#     if i in vovels:
#         vovels_count+=1
#     else:
#         consonent_count+=1
# print(vovels_count)
# print(consonent_count)

# size=int(input("Enter the size of the list: "))
# list1=[]
# list2=[]
# for i in range(size):
#     x=int(input("Enter the element: "))
#     list1.append(x)
# for i in list1:
#     if(i % 2 == 0):
#         list2.append(i)
# print(list2)

# size=int(input("Enter the size of the list: "))
# list1=[]
# for i in range(size):
#     x=int(input("Enter the element: "))
#     list1.append(x)
# key=int(input("Enter the key you want to find: "))
# for i in range(len(list1)):
#     if(list1[i] == key):
#         print("Key found at ",i)
#         break
# else:
#     print("Key not found!")

# def linear_search(arr,key):
#     for i in range(len(arr)):
#         if(arr[i] == key):
#             return True
#     return False

# tests = [
#     ([1,2,3,4,5,6],3,True),
#     ([1,23,43,42,5,4,3,42,5324,54,7654,654,543],45,False),
#     ([543,5432,76,983,7654,43,654,76543,7653,432],43,True),
#     ([5,43,234,2345,234,23456,0],5,True)
# ]

# passed=0

# for arr,key,expected in tests:
#     result=linear_search(arr,key)

#     if(result == expected):
#         print("Test case passed")
#         passed+=1
#     else:
#         print("Test case failed!")
# print(f"Total number of test cases passed: {passed}\nTotal number of test cases: {len(tests)}")

# def binary_search(arr,key):
#     arr=sorted(arr)
#     high=len(arr)-1
#     low=0
#     while(low<=high):
#         mid=high+low//2

#         if(arr[mid] == key):
#             return True
#         elif(arr[mid] < key):
#             low=mid+1
#         else:
#             high=mid-1
#     return False

# tests = [
#     ([1,2,3,4,5,6],3,True),
#     ([1,23,43,42,5,4,3,42,5324,54,7654,654,543],45,False),
#     ([543,5432,76,983,7654,43,654,76543,7653,432],43,True),
#     ([5,43,234,2345,234,23456,0],5,True)
# ]

# passed=0

# for arr,key,expected in tests:
#     result=binary_search(arr,key)

#     if(result == expected):
#         print("Test case passed")
#         passed+=1
#     else:
#         print("Test case failed!")
# print(f"Total number of test cases passed: {passed}\nTotal number of test cases: {len(tests)}")

