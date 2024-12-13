import math
n=int(input("enter the number:"))
if n<0:
	print("negative number does not have factorial")
else:
	f=math.factorial(n)
	print("factorial of",n,"=",f)

