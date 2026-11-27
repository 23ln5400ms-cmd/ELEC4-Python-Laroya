# Name: Heart C. Laroya
# Section: IV-BSIT B
# Activity: P2 - Custom Module
# Date: November 24, 2026

def validate_grades(grades):
    if not grades:
        raise ValueError("Grades list cannot be empty.")


def calculate_average(grades):
    validate_grades(grades)
    return sum(grades) / len(grades)


def determine_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(grades):
    validate_grades(grades)
    return max(grades)


def get_lowest(grades):
    validate_grades(grades)
    return min(grades)