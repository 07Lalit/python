n = int(input("Enter a no. of element in list : "))
j = [ eval(i) for i in input("Enter element in the list seprated by space : ").split()]
j = j[0:n]
s = sorted(j,reverse= False)
print("sorted list in ascending order is  : ", end="")
print(*s)
print(s)
