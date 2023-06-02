import random
import sys
import json

# while True:
#     # name = input("Name is: ")
# try:
#     print("Hello name is", sys.argv[1])
# except IndexError:
#     print("Hello, name is not defined")

# coin = random.choice(["heads", "tails"])
#
# for i in range(20):
#     print(coin)

# number = random.randint(1, 10)
# print(number)

# cards = ["Jack", "Queen", "King", "Ace", "Diamond"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

#
# if len (sys.argv) > 2:
#     sys.exit(" Way too many Args")
#
# elif len (sys.argv) < 2:
#     sys.exit(" Less Args")

# else:
#     print("Name is ",sys.argv[1])

# for arg in sys.argv[1:]:
#     print("Name is", arg)

def main():
    hello("World")
    goodbye("World!!!!!!")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"GoodBye, {name}")

if __name__ == "__main()__":
    main()

