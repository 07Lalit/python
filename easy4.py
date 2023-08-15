n = int(input("Enter a number of elment in the list : "))
j = [int(i) for i in input("Enter the items in the list seprated by space : ").split()]
j = j[0:n]
product=1
for i in j:
	product = product*i
	
print(f"list is : {j}")
print(f"Product is : {product}")

        