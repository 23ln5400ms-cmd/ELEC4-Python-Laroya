# Name: Heart C. Laroya
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 23, 2026

PASSING_GRADE = 75


def show_menu():
    print("\n===== GRADE CALCULATOR =====")
    print("[1] Enter grades")
    print("[2] View results")
    print("[3] Exit")


def ask_grade(number):
    while True:
        try:
            grade = float(input(f"Grade #{number}: "))
        except ValueError:
            print("Please enter a number only.")
            continue
        if grade < 0 or grade > 100:
            print("Grade must be from 0 to 100.")
        else:
            return grade


def enter_grades():
    grades = []
    how_many = int(input("How many grades will you enter? "))
    for n in range(1, how_many + 1):
        grades.append(ask_grade(n))
    return grades


def find_average(grades):
    return sum(grades) / len(grades)


def find_highest(grades):
    return max(grades)


def find_lowest(grades):
    return min(grades)


def check_status(average):
    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


def view_results(grades):
    average = find_average(grades)
    print("\n--- RESULTS ---")
    print(f"Average : {average:.2f}")
    print(f"Highest : {find_highest(grades)}")
    print(f"Lowest  : {find_lowest(grades)}")
    print(f"Status  : {check_status(average)}")


grades = []
running = True

while running:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        grades = enter_grades()
    elif choice == "2":
        if grades:
            view_results(grades)
        else:
            print("Please enter grades first (option 1).")
    elif choice == "3":
        print("Thank you! Goodbye.")
        running = False
    else:
        print("Invalid choice. Pick 1, 2, or 3.")
"""
 A local variable only exists inside the function where it is created. In my
 program, "average" inside view_results() is local, so the other functions
 cannot use it. A global variable is created outside every function, like
 PASSING_GRADE, so any function (such as check_status) can read it. I use a
 global for the passing mark because it never changes and many parts need it.
 """