n=int(input("enter the upperlimit:"))
i=1
sum=0
for i in range(n):
	if i%6==0 and i%4!=0:
		sum+=i
print("sum=",sum)
