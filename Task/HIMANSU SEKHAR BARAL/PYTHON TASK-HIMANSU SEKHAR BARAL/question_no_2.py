# -*- coding: utf-8 -*-
"""question no 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tSDVqe9ObsPenNArq6gq213fJIuvraXC
"""

s=input("enter the string:")
s1=sorted(s)
a=len(s1)
print(a)
for i in range(0,a):
    print(s1[i],"-->",s.count(s1[i]))