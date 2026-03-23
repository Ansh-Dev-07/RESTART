# num=list(map(int,input("Enter the numbers separated by spaces: ").split()))
s=int(input("Enter the size: "))
num=[]
for i in range(s):
    x=int(input("Enter the elements: "))
    num.append(x)
print("original number: ",num)
n=len(num)
iterations=0
for i in range(n):
    for j in range(0,n-i-1):
        iterations+=1
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(f"Sorted: {num}\nTotal iterations: {iterations}")
