n = int(input("Enter a no. of element in list : "))
j = [ eval(i) for i in input("Enter element in the list seprated by space : ").split()]
j = j[0:n]
print(f" list  : {j}")
print(f" list in reverse order is : {j[::-1]} ")


