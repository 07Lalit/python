n=int(input("Enter a no. of nested list in the list: "))
m=int(input("Enter a no. of element in each nested list : "))
cnt=1
j=[]
k=[]
for i in range(0,n):
    nl=[int(i) for i in input(f"Enter a element of  list{cnt} (sep. of spaces : ").split()]
    nl=nl[0:m]
    k.append(nl)
    nl=sorted(nl,reverse=False)
    j.append(nl)
    cnt=cnt+1
print(f"given list : {k}")
print(f"Sorted nested list in ascending order : {j} ")    
    