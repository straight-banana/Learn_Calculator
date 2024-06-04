x = float(input()) 
m = input()
y = float(input())

while(1):
    if m == "+" :
        z = x + y
        break

    if m == "-" :
        z = x - y
        break

    if m == "*" :
        z = x * y
        break

    if m == "/" :
        z = x / y
        break

    if m == "^" :
        z = x ** y
        break

    else:
        print("error")

print(f"{z}")
