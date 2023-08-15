n = int(input("Enter a no of element in the list"))
l = [ eval(i) for i in input("Enter a list separated by spaces : ").split()]
l = l[0:n]
m = []
for i in l[::-1]:
	m.append(i)
print(f" list is : {l} ")
print(f" Reversed list is : {m} ")
	


