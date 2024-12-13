names=["Rinu","Shahma","Aparna","Nafia"]
frequency=0
for name in names:
	frequency+=name.lower().count('a')
print(f"occurence of 'a' in list is {frequency}")
