n = int(input("Enter a number of elment in the list : "))
j = [int(i) for i in input("Enter the items in the list seprated by space : ").split()]
j = j[0:n]
m=[]
for num in j:
    if (num>1) :
        for i in range(2,num):
            if num%i ==0  :
                break
        else:
            m.append(num)
   
print(j)
print(f" prime no in the list are : {m}")