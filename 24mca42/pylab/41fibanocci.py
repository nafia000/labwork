def fibrecur(a,b,n):
	if n<0:
		return
	print(a)
	c=a+b
	a=b
	b=c
	fibrecur(a,b,n-1)
n=int(input("Enter the number of terms:"))
if n<0:
	print("Enter positive numbers:")
else:
	print("Fibanocci series:")
	fibrecur(0,1,n)
