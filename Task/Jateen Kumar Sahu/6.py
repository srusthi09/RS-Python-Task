n=(input("Enter a sequence of numbers:"))
arr=[]
arr1=[]
for i in n:
    m=int(i)
    arr.append(m)
print(arr)
for j in arr:
    count=0
    for k in range(1,j+1):
        if(j%k==0):
            count=count+1
    if(count==2):
        arr1.append(j)
print("The prime numbers are",arr1)
arr2=sorted(arr1)
print(arr2)
min=arr2[0]
max=arr2[len(arr2)-1]
print("The absolute difference is:",abs(min-max))





       
       
    
       
       
     
     