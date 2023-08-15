n = int(input("Enter a no. of elements in the list : "))
j=[int(i) for i in input("Enter a elements seprated by spaces : ").split()]
j=j[0:n]
l=[]
for i in j:
    l.append(i*i)
print(f"list of given elements  : {j} ")
print(f" New List containing the square of each number in the given list: {l} ")
    