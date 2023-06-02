def main():
    x = get_number("X is: ")
    print(f"X is {x}")

def get_number(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("X is not an integer")
main()