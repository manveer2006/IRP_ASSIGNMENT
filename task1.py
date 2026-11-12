
# ==========================================
# Task 1: Student Data and Control Structures
# Placement Readiness Tracker
# Roll Number: 2481078
# ==========================================

# Store student records using a list of dictionaries

students = [
    {
        "name": "Aarav",
        "roll_no": "2481001",
        "aptitude": 85,
        "verbal": 78,
        "coding": 90
    },
    {
        "name": "Rahul",
        "roll_no": "2481002",
        "aptitude": 65,
        "verbal": 72,
        "coding": 68
    },
    {
        "name": "Priya",
        "roll_no": "2481003",
        "aptitude": 92,
        "verbal": 88,
        "coding": 95
    },
    {
        "name": "Simran",
        "roll_no": "2481004",
        "aptitude": 45,
        "verbal": 55,
        "coding": 38
    },
    {
        "name": "Karan",
        "roll_no": "2481005",
        "aptitude": 75,
        "verbal": 82,
        "coding": 70
    }
]


# Function to accept and validate marks
def get_valid_score(subject):
    while True:
        try:
            score = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= score <= 100:
                return score
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Function to add a new student
def add_student():
    print("\n--- Add New Student ---")

    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    roll_no = input("Enter roll number: ").strip()

    while not roll_no:
        print("Roll number cannot be empty.")
        roll_no = input("Enter roll number: ").strip()

    student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": get_valid_score("Aptitude"),
        "verbal": get_valid_score("Verbal"),
        "coding": get_valid_score("Coding")
    }

    students.append(student)

    print("\nStudent added successfully!")


# Function to display all student records
def display_students():
    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print("------------------------------------")
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Aptitude:", student["aptitude"])
        print("Verbal:", student["verbal"])
        print("Coding:", student["coding"])

    print("====================================")


# Main program
if __name__ == "__main__":
    add_student()
    display_students()
