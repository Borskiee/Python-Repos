# Gradebook manager
# Stores and computes students grades.
gradebook = {
    "Carl": [96, 87, 91],
    "Bor": [90, 94, 84],
    "James": []
}


def add_student():
        name = input("Enter student name: ").strip().title()
        if name in gradebook:
            print("\nStudent already exists.")
            return
        elif name.replace(".", "").replace(" ", "").isalpha():
            gradebook[name] = []
            print(f"Student \n{name} added.")
        else:
            print("Please use letters and a period only.")


def add_grade():
    student = input("Enter student name: ").strip().title()
    if student in gradebook:
        try:
            grade = float(input("Enter grade: "))
        except ValueError:
            print("Please enter a number.")
            return
        if 0 <= grade <= 100:
            gradebook[student].append(grade)
        else:
            print("Please enter a grade between 0-100")
    else:
        print("Student not found.")


def view_students():
    while True:
        if not gradebook:
            print("\nNo students listed.")
            break
        for i in gradebook:
            if not gradebook[i]:
                print(f"{i} | no grade")
            else:
                print(i, gradebook[i])

        view_exit = input("\nPress 'enter' to continue: ")
        if view_exit == "":
            break
        else:
            print("Do not input to exit.")
            continue


def compute_stats():
    highest = 0
    lowest = 999
    print("\n=== Grade average ===")
    if not gradebook:
        print("No students listed.")
    for student, grade in gradebook.items():
        total = sum(grade)
        if not total:
            print(f"{student} | no grade")
        else:
            avg = total / len(grade)
            if avg > highest:
                highest = avg
            elif avg < lowest:
                lowest = avg
            print(f"{student} Average: {avg:.2f}")
    print(f"Highest avg in class: {highest:.2f}")
    print(f"Lowest avg in class: {lowest:.2f}")


def main_menu():
    while True:
        print(f"\n=== Gradebook Manager ===\n1. Add Student\n2. Add Grade\n3. View Students\n4. Compute Stats\n5. Exit")
        try:
            option = int(input("\nChoose an option: "))
        except ValueError:
            print("Please enter a number")
            continue

        if option == 1:
            add_student()
        elif option == 2:
            add_grade()
        elif option == 3:
            view_students()
        elif option == 4:
            compute_stats()
        elif option == 5:
            print("See you next time!")
            break
        else:
            print("Please select between the options.")

main_menu()

