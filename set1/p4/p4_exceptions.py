
# Name: HEART LAROYA
# Section: IV-BSIT B
# Activity: P4 - Safe Menu Program
# Date: November 27, 2026

def division():
    print("\n--- Division Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number

    except ValueError:
        print("Error: Please enter valid numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division operation finished.")


def open_file():
    print("\n--- Open Text File ---")

    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

    else:
        print("\nFile Contents:")
        print(contents)

    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Division Calculator")
        print("2. Open a File")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            division()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
