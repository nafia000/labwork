n=int(input("enter the number:"))
for i in range(1,n+1):
	for j in range(i):
		print("*",end=" ")
	print()
for i in range(n-1,0,-1):
	for j in range(i):
		print("*",end=" ")
	print()

