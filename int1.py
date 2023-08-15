n= int(input("Enter a no. of element in the list : "))
j = [str(i) for i in input("Enter a string seprated by space : ").split()]
j=j[0:n]

l=[]
for i in j:
    l.append(i[::-1])

print(f"list l1 : {j} ")

print("list  containing the intersection of both the list in ascending order is : ", *l)
        