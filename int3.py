n = int(input("Enter a no. of element in the string: "))
s=[str(i) for i in input("Enter a string seprated by spaces : ").split()]
s=s[0:n]
m=[]
for j in set(s):
    m.append(j)
print(f"list of given string : {s} ")
print(f"List of unique string : {m} ")
    