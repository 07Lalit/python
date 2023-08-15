n = int(input("Enter a no. of elements in the list : "))
j=[str(i) for i in input("Enter a String  elements seprated by spaces : ").split()]
j=j[0:n]
m=[]

for i in j:
    for ch in i:
        if ch in set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            m.append(i)
            break
         
print(f"list of given elements  : {j} ")
print(m)