n = int(input("Enter a no. of nested list  in the list : "))
t = int(input("Enter a no. of elements in each list : "))
l=[]
ml=[]

for j in range(0,n):
    j=[int(i) for i in input(f"Enter a  element  for nestded list {j+1} seprated by spaces : ").split()]
    j=j[0:t:1]
    
    l.append(j)
    ml.append(max(j))
    
    
t=max(ml)    
print(f" The final nested list is : \n {l} ")
print(f" Another list containg maximum elemnet of  the each row :\n {ml} ")
print(f" maximum of all the element : {t}")

        

 