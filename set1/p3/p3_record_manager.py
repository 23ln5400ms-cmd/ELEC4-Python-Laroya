
# Name: HEART LAROYA
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 27, 2026

students = []

student_names = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    normalized_name = name.casefold()

    if normalized_name in student_names:
        print("Student already exists. Duplicate entries are not allowed.")
    else:
        students.append(name)
        student_names.add(normalized_name)
        print(f"{name} has been added successfully.")


def remove_student():
    name = input("Enter student name to remove: ").strip()
    normalized_name = name.casefold()

    for student in students:
        if student.casefold() == normalized_name:
            students.remove(student)
            student_names.remove(normalized_name)
            print(f"{student} has been removed successfully.")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter student name or keyword to search: ").strip().casefold()

    if not keyword:
        print("Please enter a search keyword.")
        return

    results = [
        student for student in students
        if keyword in student.casefold()
    ]

    if results:
        print("\nSearch Results:")
        for number, student in enumerate(results, start=1):
            print(f"{number}. {student}")
    else:
        print("No matching student found.")


def display_students():
    if not students:
        print("\nNo students recorded yet.")
        return

    sorted_students = sorted(students, key=str.casefold)

    print("\n===== STUDENT LIST =====")

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    print(f"\nTotal Students: {len(students)}")


def display_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()


# LIST VS SET EXPLANATION:
# A list is an ordered collection that can store multiple values, including duplicates.
# In this program, I used a list to store and display the original student names.
# A set stores unique values and automatically prevents duplicate entries.
# I used a set to check whether a student name already exists, regardless of capitalization.
