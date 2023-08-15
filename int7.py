n = int(input("Enter a no. of elements in the list : "))
j=[int(i) for i in input("Enter a integer  elements seprated by spaces : ").split()]
j=j[0:n]
l=[]
avg =(sum(j)/len(j))
for i in j:
    if i > avg:
        l.append(i)
print(f"list of given elements  : {j} ")
print(f" New List containing only the numbers that are greater than the average of the original  list: {l} ")
    