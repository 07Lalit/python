n = int(input("Enter a no of element in the list : "))
l = [int(i) for i in input("Enter element of list seprated by spaces : ").split()]
l = l[0:n]
print(f"list is : {l} ")
m=[]
for i in l:
    if i%2==0:
        m.append(i)
        
print(f"Even no of element in the list : {m} ")

    