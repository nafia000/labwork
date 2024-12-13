str=input("Enter the list of words seperated by space:")
words=str.split()
length=0
for i in words:
	if len(i)>length:
		longest_word=i
		length=len(i)
		print(f"the longest word is {longest_word}and its length is {length}")
