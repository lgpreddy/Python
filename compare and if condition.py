x = int(input())
y = int(input())
if x > y:
    print("X is bigger")
# if y > x:
#     print("Y is bigger")
elif y > x:
    print("Y is bigger")
# if x == y:
#     print("Both are equal")
else:
    print("Both are equal")
score = int(input("Enter the score: "))
if score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
else:
    print('F')

def main():
    X = int(input("X is : "))
    if is_even(X):
        print("X is even")
    else:
        print("X is odd")

def is_even(n):
    return n % 2 == 0


main()





