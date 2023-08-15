n = int(input("Enter a no. of elemt in the list : "))
l =[int(i) for i in input("Enter a element seprated by spaces : ").split()]
l=l[0:n]
j=eval(input("Enter a element to check in the list : "))

if j in l:
	print(f"{j} is present in the list")
else:
	print(f"{j} is not present in the list")
print(f" Element in the list are: {l}")
