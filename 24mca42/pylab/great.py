numbers=input("enter a list of integers seperated by space:")
a=numbers.split()
l=[]
for i in a:
	l.append(int(i))
	print("list:",l)
	m_list=[]
for i in l:
	if i>100:
		m_list.append('over')
	else:
		m_list.append(i)
print("modified list:",m_list)
