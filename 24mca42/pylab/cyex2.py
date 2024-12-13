from datetime import datetime,date
import calendar
today=datetime.now()
print("Current date and time :",today)
yr=date.today()
print("Current year: ",yr.year)
print("Month of the year: ")
print(calendar.month(yr.year,yr.month))
print("Week number of the year: ",yr.strftime("%W"))
print("Weekday of the week: ",yr.strftime("%A"))
print("Day of the year: ",yr.strftime("%j"))
print("Day of the month: ",yr.strftime("%d"))
print("Day of the week: ",yr.strftime("%w"))


