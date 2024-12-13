nlist=[]
n=int(input("enter number of elements:"))
print("Enter the numbers:")
for i in range (n):
	num=int(input())
	nlist.append(num)
sum=0
for i in nlist:
	sum+=i
print("sum of all items in the list:",sum)
