n=int(input("enter total numbers:"))
listed=[]
for i in range(n):
	num=int(input("enter integers:"))
	if int(num)%2!=0:
		listed.append(num)
		print(listed)
