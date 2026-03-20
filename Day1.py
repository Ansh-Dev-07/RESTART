#reverse a string without using slicing.

#using for loop
# str1=input("Enter a string: ")
# print("The reverse String is: ",end=' ')
# for i in range(len(str1)-1,-1,-1):
#     print(str1[i],end='')

#using while loop
# str2=""
# rev=""
# i=len(str2)-1
# while(i>=0):
#     rev=rev+str2[i]
#     i-=1
# print(rev)

# if(str2 == rev):
#     print("palindrome")
# else:
#     print("not palindrome")

#find second largest number in a list.

#list1=[1,23,23,578]
#case 1:
# list1=[3,1,4,2]
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
