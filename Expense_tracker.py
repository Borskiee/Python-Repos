#Expense Tracker = 1000
balance = 10000
expenses = []
categories = ["Food", "Transport", "Bills", "Entertainment", "Shopping", "Misc"]

def add_expense():
    global balance
    if not categories:
        print("No categories available.")
        return

    # --- Select category ---
    print("\nCategories:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")

    while True:
        try:
            select_category = int(input("\nSelect category: "))
            if 1 <= select_category <= len(categories):
                category = categories[select_category - 1]
                break
            else:
                print("Please select a number between the options.")
        except ValueError:
            print("Please enter a valid number.")

    # --- Enter amount ---
    while True:
        try:
            amount = int(input("Enter amount (Type 0 to exit): "))
            if amount == 0:
                break
        except ValueError:
            print("Invalid input")
            continue

        if amount < 0:
            print("Amount must be greater than 0.")

        if amount > balance:
            print("Insufficient funds.")

        balance -= amount
        print(f"\nDeducted ${amount} from your balance.")
        break

    # --- Create expense and append ---
    expense = {"amount": amount, "category": category}
    switch = False
    for x in expenses:
        if x['category'] == expense['category']:
            x['amount'] += expense['amount']
            switch = True
            break

    if not switch and amount <= balance:
        expenses.append(expense)


def view_expenses():
    while True:
        if not expenses:
            print("No expenses.")
            return
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['category']} - ${expense['amount']}")
        try:
            mod = int(input("\nSelect expense to remove (type 0 to exit): "))
            if 1 <= mod <= len(expenses):
                removed = expenses.pop(mod -1)
                print(f"\nRemoved {expense['category']} - ${removed['amount']}")
                continue
            elif mod == 0:
                return
            else:
                print("Please select between the options.")

        except ValueError:
                print("Invalid input")


def view_summary():
    if not expenses:
        print("No expenses yet.")
    else:
        total = 0

        print("\n=== Expenses ===")
        for expense in expenses:
            total += expense['amount']
            print(f"{expense['category']} - {expense['amount']}")
        print(f"Total expense: ${total}")
        input("\nPress 'Enter' to continue...")

def main_menu():
    while True:
        try:
            menu = int(input(f"\n=== Expense Calculator ===\nCurrent balance: ${balance}\n1. Add expense\n2. View expenses\n3. View summary\n4. Exit\n\nSelect: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        if menu == 1:
            add_expense()
        elif menu == 2:
            view_expenses()
        elif menu == 3:
            view_summary()
        elif menu == 4:
            print("See you next time!")
            break
        elif menu == 5:
            print(balance)
        else:
            print("Please select between the options.")

main_menu()