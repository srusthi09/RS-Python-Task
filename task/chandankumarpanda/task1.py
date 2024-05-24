import numpy as np
import pandas as pd
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!kaggle datasets download -d arshid/iris-flower-dataset
import zipfile
zip_ref = zipfile.ZipFile('/content/iris-flower-dataset.zip', 'r')
zip_ref.extractall('/content')
zip_ref.close()
df=pd.read_csv('/content/IRIS.csv')
df.shape
df.head()
df['sepal_length'].sum()
df['sepal_length'].max()
df['sepal_length'].min()





TRANSPOSE
import numpy as np
r=int(input("enter the row:"))
c=int(input("enter the col:"))
a=[]
b=r*c
for i in range(0,b):
    element=int(input("enter the element of matrix:"))
    a.append(element)
print(a)
b=np.array(a).reshape(r,c)




print(np.transpose(b))




ARRAY2
import array as arr
le=int(input("enter the length of no:"))
pr1=[]

num=arr.array('i',[])
for i in range(0,le):
    element=int(input("enter the no:"))
    num.append(element)
print(num)

pr=list(num)
pr.sort()
for i in range(0,len(pr)):
    a=0
    for j in range(2,pr[i]):

        if pr[i]%j==0:
            a=1
            break
    if a==0:
            pr1.append(pr[i])


print(pr1)
if pr1[0]==2:
    diff=pr1[-1]-pr1[1]
elif pr1[0]!=2:
    diff=pr1[-1]-pr[0]
print(diff)





dictionary
l=int(input("enter the no of element:"))
li=[]
for i in range (0,l):
    element=input("enter the element:")
    li.append(element)
print(li) 
key=[]
for i in range(0,l):
    element=li[i]
    key.append(element)
print(key)
value=[]
for i in range(0,l):
    re=li.count(li[i])
    value.append(re)
print(value)
d1={i:j for (i,j) in zip(key,value)}
print(d1)






array1
import array as arr
number=int(input("enter length of  the number:"))
digit=arr.array('i',[])
for i in range (0,number):
    element=int(input("enter the number:"))
    digit.append(element)
print(digit)
li=list(digit)
print(li)
temp=""
for i in range(0,len(li)):
    temp=temp+str(li[i])
print(temp)
num=int(temp)
num=num+1
num1=str(num)

li1=list(num1)
li2=[]
for i in range (0,len(li1)):
    element=int(li1[i])
    li2.append(element)
print(li2)

digit2=arr.array('i',[])
for i in range(0,len(li2)):
    element=li2[i]
    digit2.append(element)
print(digit2)






primefactor
prime factor=[]
mrp=int(input('enter the amount:'))

for i in range (2,mrp+1):
  if mrp%i==0:
    a=0
    for j in range(2,i):
      if i%j==0:
        a=1
        break
    if a==0:
      prime_factor.append(i)
print(prime_factor)
min=prime_factor[0]
alfipaid=min
roypaid=mrp-min
print(alfipaid)
print(roypaid)




frequency
s=input("enter the string:")
s1=sorted(s)
print(type(s1))
for i in range(0,len(s1)):
    print(s1[i],"-->",s.count(s1[i]))





anagram
s= input("enter the string s:")
t = input("enter the string t :")
s1=s.lower()
t1=t.lower()
print(s1)
print(t1)
s2=sorted(s1)
print(s2)
t2=sorted(t1)
print(t2)
result=s2==t2
print(result)





ARRAY3

import array as arr
number=int(input("enter length of  the number:"))
digit=arr.array('i',[])
for i in range (0,number):
    element=int(input("enter the number:"))
    digit.append(element)
print(digit)
li=list(digit)
print(li)
temp=""
for i in range(0,len(li)):
    temp=temp+str(li[i])
print(temp)    
num=int(temp)
num=num+1
num1=str(num)

li1=list(num1)
li2=[]
for i in range (0,len(li1)):
    element=int(li1[i])
    li2.append(element)
print(li2)    

digit2=arr.array('i',[])
for i in range(0,len(li2)):
    element=li2[i]
    digit2.append(element)
print(digit2)    

