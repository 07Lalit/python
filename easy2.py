n,m= input("Enter a no of element in the list1 and list2 (sep by space) : ").split()
n,m =int(n),int(m)
j = [int(i) for i in input("Enter element of list1 seprated by spaces : ").split()]
j = j[0:n]
k = [int(i) for i in input("Enter element of list2 seprated by spaces : ").split()]
k = k[0:m]
m=[]
print(f"list 1 : {j} ")
print(f"list 2 : {k} ")
for i in j:
    if i in k:
        m.append(i)
print(f" common element in both list are : {m} ")


        