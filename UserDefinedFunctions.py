# def main():
#     x=int(input("X is : "))
#     name = input("Enter name: ")
#     cube = (hello(x))
#     print(f"Name is {cube} times {name} ")
#
# def hello(x):
#     return x*x*x


# x = (input("X is: "))
# print(f"X is {x}")

# def main():
#     while True:
#         try:
#             X = int(input("X is: "))
#             print(f"X is {squared(X)}")
#         except:
#             print(" X is not an int")
#             break
#
# def squared(n):
#     return n * n
#
# if __name__ == "__main()__":
#     main()

def main():
    greeting = hi("How are you?", "What's up?")
    print(greeting)

def hi(*args):
   result =  "Hello", *args
   return result

main()

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

def dresses(pants, shirts):

    print(f"I have to get {pants} no of pants ")
    print(f"I have to pack {shirts} no of shirts")
    print("I need a big bag")
    print("That's all")

pants = int(input("X: "))
shirts= int(input("Y is: "))
dresses(pants, shirts)

def add(a,b):
    sum = int (a) + int(b)
    return sum

area = add(3,5)
print(area/2)