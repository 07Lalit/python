  # 1.Write a program to find the sum of all elements in a list.

n = int(input("Enter a no of element in the list : "))
j = [eval(i) for i in input("Enter a integer elment in the list seprated by spaces : ").split()]
j = j[0:n]
print(f"list is : {j} ")
print(f"Sum of list is : {sum(j)}")

