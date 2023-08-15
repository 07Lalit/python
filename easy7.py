n = int(input("Enter a no. of element in the list : "))
l = [str(i) for i in input("Enter a string seprated by space : ").split()]
l=l[0:n]
m=[]
for i in l:
    if (i==i[::-1]):
        m.append(i)
    
print(f"list of string is : {l} ")
print(f"list of string Which are palindrome are : {m} ")
        