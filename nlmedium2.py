n=int(input("Enter a no. of nested list in the list1: "))
m=int(input("Enter a no. of element in each nested list of list1 : "))
n1=int(input("Enter a no. of nested list in the list2: "))
m1=int(input("Enter a no. of element in each nested list of  list2 : "))

k=[]
j=[]
p=[]
lg=[]
cnt=1

for i in range(0,n):
    li=1
    nl=[int(i) for i in input(f"Enter a element of  list{li} ka {cnt} (sep. of spaces : ").split()]
    nl=nl[0:m]
    cnt=cnt+1
   
    k.append(nl)
    
    
cnt=1    
for i in range(0,n1):
    li=2
    nl=[int(i) for i in input(f"Enter a element of  list{li} ka {cnt} (sep. of spaces : ").split()]
    nl=nl[0:m1]
    cnt=cnt+1
    p.append(nl)


print(f" given list : \n{k}")
print(f" nested list of list : \n{p}")
g=[]
g= k+p 
t=[]
t.append(k)
t.append(p)
print(f"New list :\n {g} ")   
print(f"New list :\n {t} ") 
print(t[0][0][0])
print(t[0][0][1])
print(t[0][1][0])
print(t[0][1][1])
print(t[1][0][0])
print(t[1][0][1])
print(t[1][1][0])
print(t[1][1][1])
print(" \n\n")

print(sum(t[0][0][0])+t[1][0][0]) )
print("\t\t\t\tThank you")