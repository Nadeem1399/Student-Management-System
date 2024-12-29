import csv
import os

# File path for storing student data
file_path = 'studentmanagement.csv'

# Check if the file exists, create it with header if not
def initialize_file():
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll Number', 'Name', 'Marks'])

# Add a new student record
def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll_number, name, marks])
    print("Student added successfully!")

# Update an existing student record
def update_student():
    roll_number = input("Enter the roll number of the student to update: ")
    found = False

    # Read all student records
    students = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            students.append(row)

    # Search for the student by roll number
    for student in students:
        if student[0] == roll_number:
            found = True
            new_name = input(f"Enter new name for {student[1]}: ")
            new_marks = input(f"Enter new marks for {student[1]}: ")
            student[1] = new_name
            student[2] = new_marks
            print("Student record updated successfully!")
            break

    # If student is found, update the file
    if found:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll Number', 'Name', 'Marks'])  # Write header again
            writer.writerows(students)
    else:
        print("Student not found!")

# Delete a student record
def delete_student():
    roll_number = input("Enter the roll number of the student to delete: ")
    found = False

    # Read all student records
    students = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            students.append(row)

    # Search for the student by roll number
    for student in students:
        if student[0] == roll_number:
            found = True
            students.remove(student)
            print("Student record deleted successfully!")
            break

    # If student is found, update the file
    if found:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll Number', 'Name', 'Marks'])  # Write header again
            writer.writerows(students)
    else:
        print("Student not found!")

# Search for a student by roll number or name
def search_student():
    search_type = input("Search by (1) Roll Number or (2) Name: ")
    if search_type == '1':
        roll_number = input("Enter the roll number to search: ")
        found = False
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == roll_number:
                    print(f"Student found: Roll Number: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
                    found = True
                    break
        if not found:
            print("Student not found!")
    elif search_type == '2':
        name = input("Enter the name to search: ").lower()
        found = False
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if name in row[1].lower():
                    print(f"Student found: Roll Number: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
                    found = True
        if not found:
            print("Student not found!")
    else:
        print("Invalid search type!")

# Display the main menu
def display_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Main program
if __name__ == "__main__":
    initialize_file()
    display_menu()
