x = float(input("value: ")) #int can be used to make it simpler
y = float(input("Value: "))

z = round(x % y , 2) #z = x % y (if you use int)

print(f"{z:,}")