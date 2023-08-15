n = int(input("Enter a no. of element in the list : "))
l = [int(i) for i in input("Enter a string seprated by space : ").split()]
l=l[0:n]
m=[]
for i in l:
    j= l.index(i)
    m.append(sum(l[ 0 : j+1 ] ))
    
print(f"list of string is : {l} ")
print(f"list of string Which are palindrome are : {m} ")
        