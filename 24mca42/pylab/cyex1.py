import calendar
year=int(input("enter a year :"))
if calendar.isleap(year):
	print(f"{year} is a leap year")
else:
	print(f"{year} is not a leap year")
