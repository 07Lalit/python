n=int(input("Enter a no. of nested list in the list: "))
m=int(input("Enter a no. of element in each nested list : "))
cnt=1
j=[]
k=[]
s=[]
g=[]
for i in range(0,n):
    nl=[int(i) for i in input(f"Enter a element of  list{cnt} (sep. of spaces : ").split()]
    nl=nl[0:m]
    k.append(nl)
    j.append(nl)
    cnt=cnt+1

for i in range(0,n):
    for j in range(0,n):
        s.append(k[j][i])
        
    g.append(s)
    s=[]    
print(f" given list : {k}")
    
print(f"list containg transpose of list : \n {g} ")    