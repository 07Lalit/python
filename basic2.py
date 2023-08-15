i = int(input("Enter a no. of element is list: "))
n = [int(i) for i in input("Enter a element in the list seprated by space : ").split()]
n=n[0:i]
print(f"List is :{n}" )
print(f"Maximum of list : {max(n)} ")