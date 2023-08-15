n = int(input("Enter a no. of elements in the list : "))
j=[str(i) for i in input("Enter a string elements seprated by spaces : ").split()]
j=j[0:n]
m=[]
s=set("0123456789")

for i in j:
    for ch in i:
        if ch in s :
            m.append(i)
            break
        
print(f"Orginal list : {j} ")
print(f" New list of elements containing atleast 1 digit:{m}  ")


 