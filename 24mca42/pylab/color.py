colorlist1=input("Enter colors for list1 seperated by space:")
colorlist2=input("Enter colors for list2 seperated by space:")
colorlst1=colorlist1.split()
colorlst2=colorlist2.split()
newlist=[color for color in colorlst1 if color not in colorlst2]
print(f"list of colors from list1 and not contained in list2 are:{newlist}")

