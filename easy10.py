n = int(input("Enter a no. of element in the list : "))
l = [int(i) for i in input("Enter a string seprated by space : ").split()]
l=l[0:n]
m=[]
for i in l:
    if i%3==0 or i%5==0:
        m.append(i)
print(f"list of string is : {l} ")
print(f"list of string Which are palindrome are : {m} ")
        