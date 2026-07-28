# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student(records):
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: ID must be a number.")
        return

    try:
        count = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a valid number of scores.")
        return

    if count < 0:
        print("Error: Number of scores cannot be negative.")
        return

    scores = []
    for i in range(1, count + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                scores.append(score)
                break
            except ValueError:
                print("Error: Please enter a valid numeric score.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    records.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(records):
    if not records:
        print("No student records available.")
        return

    print("--------------------------------------------------")
    print(f"{'Name':<15} {'ID':<12} {'Scores':<20} {'Average'}")
    print("--------------------------------------------------")
    for student in records:
        scores_text = ", ".join(str(int(score)) if score.is_integer() else str(score) for score in student["scores"])
        if student["scores"]:
            avg_score = round(sum(student["scores"]) / len(student["scores"]), 2)
            avg_text = f"{avg_score:.2f}"
        else:
            avg_text = "0.00"
        print(f"{student['name']:<15} {student['id']:<12} {scores_text:<20} {avg_text}")
    print("--------------------------------------------------")


def calculate_average_score(records):
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: ID must be a number.")
        return

    student = next((record for record in records if record["id"] == student_id), None)
    if student is None:
        print("Error: Student ID not found.")
        return

    scores = student["scores"]
    if not scores:
        average = 0.00
    else:
        average = round(sum(scores) / len(scores), 2)
    print(f"{student['name']}'s average score: {average:.2f}")


def display_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    records = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_all_students(records)
        elif choice == "3":
            calculate_average_score(records)
        elif choice == "4":
            break
        else:
            print("Error: Please enter a choice from 1 to 4.")
        print()


if __name__ == "__main__":
    main()

