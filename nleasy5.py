n = int(input("Enter a no. of nested list in the list: "))
m = int(input("Enter a no. of element in each list: "))
l=[]
k=[]
cnt=1
prd=1
while(n!=0):
    d=[int(i) for i in input(f"Enter a list{cnt} : ").split()]
    d=d[0:m]
    l.append(d)
    n=n-1
    cnt+=1 
    for i in d:
        prd=prd*i
    k.append(prd)
    prd=1
print(f"nested list l is : {l} ")
print(f" product of each row of nested list l is : {k} ")