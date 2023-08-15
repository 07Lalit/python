n,m = input("Enter a no of element in the list l1 an l2 : ").split()
n,m= int(n),int(m)

j = [ eval(i) for i in input("Enter a list l1 separated by spaces : ").split()]
j = j[0:n]
k = [ eval(i) for i in input("Enter a list l2 separated by spaces : ").split()]
k = k[0:m]

print(f" list l1: {j} ")
print(f" list l2: {k} ")
print(f" list l1 + l2 : {j+k} ")

