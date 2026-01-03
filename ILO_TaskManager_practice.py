'''Ask the user to add, view, or remove tasks.

Store tasks in a list.

Use functions for each responsibility:

Input → get user action or task

Logic → add/remove/view tasks

Output → print the current tasks cleanly

Keep looping until the user chooses to exit.

Optional: limit the number of tasks to 5–10 (to practice counters).'''

tasks = [
    {"name": "Run", "status": "incomplete"}
]


def validate_input(text):
        if not text:
            return False, "Input cannot be empty."

        if not text[0].isalpha():
            return False, "First character must be a letter."

        if not text[1:].isalnum():  # rest can be letters or numbers
            return False, "Only letters and numbers allowed after the first character."

        return True, ""  # valid input

def get_user_input():
    while True:
        user_text = input("Choose between the options (add, view, remove): ")
        is_valid, error = validate_input(user_text)

        if not is_valid:
            print(error)
            continue

        return user_text.lower()  # always return lowercase for easier comparison

get_user_input()