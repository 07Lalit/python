n,m = input("Enter a no. of element in the list1 and list2 sep. by space : ").split()
n,m = int(n),int(m)
j=[int(i) for i in input("Enter a string seprated by spaces : ").split()]
j=j[0:n]
k=[int(i) for i in input("Enter a string seprated by spaces : ").split()]
k=k[0:m]
l=[]
for i in j:
    if i not in k:
        l.append(i)
for p in k:
    if p not in j:
        l.append(p)
    
print(f"list1  : {j} ")
print(f"list2 : {k} ")
print(f" List containing the elements that are only in one of the two lists: {l} ")
    