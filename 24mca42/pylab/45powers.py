
twox=lambda x:2**x
terms=int(input("Enter the number of terms: "))
power_of_2=list(map(twox,range(terms)))
print("Power of 2 upto ",terms," terms:")
for i in range(terms):
        print(f"2^{i}={power_of_2[i]}")



lt=[]
n=int(input("Enter no.of terms:"))
for i in range(n):
        terms=int(input("Enter terms: "))
        lt.append(terms)
twox=lambda x:2**x
power_of_2=map(twox,lt)
print("Powers of 2:")
power_fnctn_list=list(power_of_2)
print(power_fnctn_list)





