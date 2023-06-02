x = int(input("What's X: "))
y = int(input("What's y: "))
a = x + y
b = x - y

if (x or y ) != 0:
    try:
        c = x / y
        d = x % y
    except ZeroDivisionError:
        c = "\nOne of them is zero"
        d = "\nOne of them is Zero"



print(a, b, c, d, sep = " AND ")
