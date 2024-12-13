import math
a=float(input("Enter coefficient of x^2:"))
b=float(input("Enter coefficient of x:"))
c=float(input("Enter the constant:"))
print(f"quadratic equation:{a}x^2+{b}x+{c}=0\n")
d=b**2-4*a*c
if d==0:
	root=b/(2*a)
	print("The roots are real and equal")
	print(f"The root is{root:2f}\n")
elif d>0:
	root1=(b+math.sqrt(d))/(2*a)
	root2=(b-math.sqrt(d))/(2*a)
	print("The roots are real and different")
	print(f"the roots are{root1}and{root2}\n")
elif d<0:
	real_part=b/(2*a)
	img_part=math.sqrt(-d)/(2*a)
	print("The roots are complex")
	print(f"The roots are {real_part:2f}+{img_part:2f}j and{real_part:2f}-{img_part:2f}j\0")
else :
	print("The equation has no real roots!\n")
