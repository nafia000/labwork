text=input("enter text:")
words=text.split()
word_count={}
for i in words:
	i=i.lower()
if i in word_count:
	word_count[i]+=1
else:
	word_count[i]=1
	print(f"word occurences are:{word_count}")
