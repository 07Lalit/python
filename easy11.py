n,m = input("Enter a no. of element in the list1 and list2 : ").split()
n,m = int(n),int(m)
j = [int(i) for i in input("Enter a list1 seprated by space : ").split()]
j=j[0:n]
k = [int(i) for i in input("Enter a list2 seprated by space : ").split()]
k=k[0:m]
l=[]
for i in j:
    if i in k:
        l.append(i)
s= sorted(l,reverse=False)
print(f"list l1 : {j} ")
print(f"list l2 : {k} ")
print(f"list  containing the intersection of both the list in ascending order is : {s} ")
        