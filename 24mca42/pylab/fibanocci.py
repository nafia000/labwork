N=int(input("enter the number of terms:"))
num1=0
num2=1
next_num=num1
count=1
while count<=N:
	print(next_num,end=" ")
	count+=1
	num1,num2=num2,next_num
	next_num=num1+num2

