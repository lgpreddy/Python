# def main():
#     name = input("Enter the name: ")
#     house = input("Enter the house: ")
#     print(f"Name is {name} and house is {house}")
#
# main()


def main():
    # name = get_student()
    # house = get_student()
    n,h = get_student()
    print(f"Name {n} from {h}")

# def get_name():
#     return input("Name: ")
#
# def get_house():
#     house = input("House: ")
#     return house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name,house)

if __name__ == "__main__":
    main()


