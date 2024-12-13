str=input("enter a string:")
count={}
for char in str:
	if char in count:
		count[char]+=1
	else:
		count[char]=1
print(count)
