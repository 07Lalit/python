n=int(input("Enter a no. of nested list in the list: "))
m=int(input("Enter a no. of element in each nested list : "))
cnt=1
j=[]
k=[]
for i in range(0,n):
    nl=[int(i) for i in input(f"Enter a element of  list{cnt} (sep. of spaces : ").split()]
    nl=nl[0:m]
    k.append(nl)
    cnt+=1
    
s=[int(k[i][j]) for i in range(0,n) for j in range(0,m) if k[i]==k[j]]
j.append(s)
    
 
print(f" given list : {k}")
print(f" new list containing the elements that are on the diagonal of the original list : \n {j} ")    
    