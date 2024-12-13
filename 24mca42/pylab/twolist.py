n=int(input("Enter number of integers to input:"))
list1=[]
for i in range(n):
	num1=int(input("Enter integers:"))
	list1.append(num1)
n=int(input("Enter number of integers of integers to input:"))
list2=[]
for i in range(n):
	num2=int(input("Enter integers:")) 
	list2.append(num2)
if len(list1)==len(list2):
	print("lists are of same length")
else:
	print("lists are of different length")
if sum(list1)==sum(list2):
	print("the list sum have same value")
else:
	print("the lists do not have same value")
	common=set(list1)&set(list2)
if common:
	print(f"common values in both list are:{common}")
else:
	print("these are no common values in both lists")
