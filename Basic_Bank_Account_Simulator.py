# Basic Bank Account Simulator

balance = 0.0

def show_balance():
    print(f"\nCurrent balance: ${balance:.2f}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Amount must be positive.")
    except ValueError:
        print("Invalid input.")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient funds.")
        elif amount > 0:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Amount must be positive.")
    except ValueError:
        print("Invalid input.")

def main_menu():
    while True:
        print("\n=== Bank Account Menu ===")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
