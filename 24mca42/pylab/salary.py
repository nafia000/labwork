basic_pay=float(input("enter the basic pay:"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total=hra+ta+basic_pay
print(f"Basic pay:{basic_pay}\nHR:{hra}\nTA:{ta}\n Total:{total}")
