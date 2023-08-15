i = int(input("Enter a no. of element is list: "))
n = [eval(i) for i in input("Enter a element in the list seprated by space : ").split()]
n=n[0:i]
print(f"List is :{n}" )
print(f"Number  of element in list : {len(n)} ")
print(*n)