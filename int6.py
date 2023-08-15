n = int(input("Enter a no. of elements in the list : "))
j=[str(i) for i in input("Enter a  String elements seprated by spaces : ").split()]
j=j[0:n]
l=[]
for i in j:
    l.append(i[::-1])
print(f"list of given elements  : {j} ")
print(f" New List containing the reverse of each elements in the  given list: {l} ")
    