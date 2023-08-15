n = int(input("Enter a no. of nested list  in the list : "))
t = int(input("Enter a no. of elements in each list : "))
l=[]
sum=0

for j in range(0,n):
    j=[int(i) for i in input(f"Enter a  element  for nestded list {j+1} seprated by spaces : ").split()]
    j=j[0:t:1]
    for k in j:
        sum=sum+k
    l.append(j)
    
    
print(f" The final nested list is : \n {l} ")
print(f"sum of all the element of nested list is : {sum}")

        

 