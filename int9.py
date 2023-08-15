n = int(input("Enter a no. of elements in the list : "))
j=[str(i) for i in input("Enter a integer elements seprated by spaces : ").split()]
j=j[0:n]
m=[]

for i in j:
    for ch in i:
        k= j.index(i)
        for d in j[k+1::1]:
            if ch in set(d):
                m.append(i)
                break
            
         
print(f"list of given elements  : {j} ")
print(m)