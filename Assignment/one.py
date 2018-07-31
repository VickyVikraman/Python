from _sqlite3 import Row
row=int(input("Enter the number of rows"))
column=int(input("Enter the number of columns"))
mat=[]
for i in range(0,row):
    mat.append([])
    for j in range(0,column):
      mat[i].append(int(input()))

for i in range(0,row):
    for j in range(0,column):
        print(mat[i][j],end=' ')
#     print()