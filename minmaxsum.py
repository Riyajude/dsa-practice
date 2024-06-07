def minmaxsum(arr):
    l=len(arr)
    min=arr[0]
    max=arr[0]
    for i in range(l):
        if arr[i]<min:
            min=arr[i]
            
    for j in range(l):
        if arr[j]>max:
            max=arr[j]
    
    sum=max+min
    return sum,min,max
  
n=int(input("Enter size"))
l=[n]  
print("Enter elements")
for i in range(n):
    x=int(input("element:"))
    l.append(x)
print(l)
sum,min,max=minmaxsum(l)
print(sum,min,max)
