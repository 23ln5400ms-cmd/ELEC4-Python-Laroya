
# Name: Heart C. Laroya
# Section: IV-BSIT 
# Activity: P2 - Custom Module
# Date: November 24, 2026

import student_utils
from student_utils import calculate_average

from datetime import datetime

print("===================================")
print("       STUDENT GRADE REPORT")
print("===================================")


student_name = input("Enter student name: ")

while True:
    try:
        number_of_grades = int(input("How many grades will you enter? "))

        if number_of_grades > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


grades = []

for i in range(number_of_grades):
    while True:
        try:
            grade = float(input(f"Enter grade {i + 1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


average = calculate_average(grades)
status = student_utils.determine_status(average)
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)

print("\n===================================")
print("          GRADE RESULTS")
print("===================================")

print("Student Name:", student_name)
print("Grades:", grades)
print("Average:", round(average, 2))
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", status)


print("Report Generated:", datetime.now().strftime("%B %d, %Y %I:%M %p"))

print("===================================")
