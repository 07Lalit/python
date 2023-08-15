n = int(input("Enter a no of element in the list : "))
l = [ eval(i) for i in input("Enter a list separated by spaces : ").split()]
l = l[0:n]
print(f" List is : {l} ")
s= sorted(l)
j = sorted(l,reverse=True)
print(f" Sorted List is : {s} ")
print(f"Second element of the list is : {j[-2]}")
    
