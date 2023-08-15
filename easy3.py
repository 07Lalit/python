n = int(input("Enter a number of elment in the list : "))
j = [str(i) for i in input("Enter the items in the list seprated by space : ").split()]
j = j[0:n]
m=[]
for i in j:
    if len(i)>=5:
        m.append(i)
print(j)
print(f" List of element of string having length greter than or equal to 5 are : {m}")
        