n = int(input("Enter a no. of elements in the list : "))
j=[str(i) for i in input("Enter a integer elements seprated by spaces : ").split()]
j=j[0:n]
m=[]
n=1
k = sorted(j,reverse=True,key=len)
print(k)

for i in k:
    if len(k[0])==len(i):
        m.append(i)

        
print(m)
    