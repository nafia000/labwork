n=int(input("enter the number:"))
fact=1
print("Factors are:")
while fact<=n:
	if n%fact==0:
		print(fact,end=" ")
	fact=fact+1
