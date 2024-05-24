np=int(input("Enter the number of products:"))
mrp=int(input("Enter the MRP of each product:"))
arr1=[]

for i in range(1,mrp+1):
    if(mrp%i==0):
            count=0
            for j in range(1,i+1):
                   if(i%j==0):
                          count=count+1
            if(count==2):
                arr1.append(i)
print("The prime factors are",arr1)
arr2=sorted(arr1)
alfi=np*arr2[0]
roy=np*(mrp-alfi)
print("Alfi pays",alfi,"and Roy pays",roy)



