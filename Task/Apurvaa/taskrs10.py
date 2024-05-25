a=int(input("Enter the number of rows:"))
b=int(input("Enter the number of columns:"))
if(a!=b):
    raise ValueError("Not a square matrix!")
else:
 print("Enter the elements row by row:")
 mat = [[int(input()) for x in range (a)] for y in range(b)]
print(mat)
def trans(k,l):
 for i in range(a): 
  for j in range(b): 
   mat_trans[j][i] = mat[i][j] 
mat_trans=[[0 for x in range(a)] for y in range(b)]
trans(mat,mat_trans)
print("Result matrix is") 
for i in range(a): 
 for j in range(b): 
  print(mat_trans[i][j], " ", end='')   