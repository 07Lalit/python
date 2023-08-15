n = int(input("Enter a number of elment in the list : "))
j = [str(i) for i in input("Enter the items in the list seprated by space : ").split()]
j = j[0:n]
m=[]
for i in j:
    if i[0] in 'aA':
        m.append(i)
print(f" list of element in the string : {j}")
print(f" List of element of string start with 'a' or 'A' are  : {m}")
        