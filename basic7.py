n = int(input("Enter a no. of element in list : "))
j = [ int(i) for i in input("Enter element in the list seprated by space : ").split()]
j = j[0:n]
k = int(input("Enter the element to check index : "))

if k not in j:
    print(f"{k} is not present in the list")
else:
    print(f"Index of {k} is  {j.index(k)}")
print(f" list of element is : {j} ")