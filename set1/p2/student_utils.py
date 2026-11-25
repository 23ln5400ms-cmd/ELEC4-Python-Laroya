
# Name: Heart C. Laroya
# Section: IV-BSIT 
# Activity: P2 - Custom Module
# Date: November 24, 2026

# Function to calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function to determine pass or fail
def determine_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function to get the highest grade
def get_highest(grades):
    return max(grades)


# Function to get the lowest grade
def get_lowest(grades):
    return min(grades)
