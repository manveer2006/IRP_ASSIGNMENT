
# ==========================================
# Task 2: Functions and Performance Analysis
# Placement Readiness Tracker
# Roll Number: 2481078
# ==========================================

# Import student records and input function from Task 1
from task1 import students, add_student


# Function 1: Calculate average marks
def average(student):
    total = (
        student["aptitude"]
        + student["verbal"]
        + student["coding"]
    )

    return total / 3


# Function 2: Assign grade based on average
def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


# Function 3: Find the highest-scoring student
def top_scorer(students):
    return max(students, key=average)


# Function 4: Find students needing practice
def needs_practice(students, limit=40):
    return [
        student for student in students
        if average(student) < limit
    ]


# Function to display the performance report
def display_results(students):

    print("\n" + "=" * 85)
    print("                 PLACEMENT READINESS REPORT")
    print("=" * 85)

    print(
        f"{'Name':<12}"
        f"{'Roll No':<14}"
        f"{'Aptitude':<12}"
        f"{'Verbal':<10}"
        f"{'Coding':<10}"
        f"{'Average':<10}"
        f"{'Grade':<15}"
    )

    print("-" * 85)

    for student in students:

        avg = average(student)
        student_grade = grade(avg)

        print(
            f"{student['name']:<12}"
            f"{student['roll_no']:<14}"
            f"{student['aptitude']:<12}"
            f"{student['verbal']:<10}"
            f"{student['coding']:<10}"
            f"{avg:<10.2f}"
            f"{student_grade:<15}"
        )

    print("-" * 85)

    # Display top scorer
    topper = top_scorer(students)

    print("\nTOP PERFORMER")
    print("Name:", topper["name"])
    print("Roll Number:", topper["roll_no"])
    print("Average:", round(average(topper), 2))

    # Display students needing practice
    practice_students = needs_practice(students)

    print("\nSTUDENTS NEEDING PRACTICE")

    if practice_students:
        for student in practice_students:
            print(
                student["name"],
                "- Average:",
                round(average(student), 2)
            )
    else:
        print("No students need additional practice.")

    print("=" * 85)


# Main program
if __name__ == "__main__":

    # Add a student for this program's report
    add_student()

    # Display complete performance report
    display_results(students)
