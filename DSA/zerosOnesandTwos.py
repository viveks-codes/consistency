a = [0,1,0,1,0,2,0,1]
n = len(a)
n1, n2,nz = 0,0,0
for i in range(n):
     if a[i]==1:
         n1+=1
     elif a[i]==0:
         nz+=1
     else:
         n2+=1
a[:] = [0] * nz + [1] *n1 + [2] * n2
print(a)