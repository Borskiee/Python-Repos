# Input
def num_func():
    while True:
        try:
            num_input = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
            return num_input
        except ValueError:
            print("Please enter a number.")

# Logic
def compute_sum(n):
    return sum(n)

def compute_avg(a):
    return sum(a) / len(a)

def compute_max(n):
    return max(n)

def compute_min(n):
    return min(n)


def main_menu(option, n):
    if option == "1":
        print(f"Sum: {compute_sum(n)}")
    elif option == "2":
        print(f"Average: {compute_avg(n):.2f}")
    elif option == "3":
        print(f"Highest: {compute_max(n)}")
    elif option == "4":
        print(f"Lowest: {compute_min(n)}")
    else:
        print("Please select between the options.")


# Output
numbers = num_func()

while True:
    print("\nChoose an option:")
    print("1. Sum")
    print("2. Average")
    print("3. Highest")
    print("4. Lowest")
    print("5. Exit")

    choice = input("Enter a choice: ")

    if choice == "5":
        print("Goodbye!")
        break
    else:
        main_menu(choice, numbers)
