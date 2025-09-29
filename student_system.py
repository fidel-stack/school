"""
def show_menu():
    print("\n===== Student Record System=====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Edit student")
    print("5. Delete student")
    print("6. Exit")


students = []

def add_student():
    name = input("Enter student name: ")
    reg_no = input("Enter registrtion number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "reg_no": reg_no,
        "course": course
    }
    students.append(student)
    print(f"✅{name} added successfully!")

def view_students():
    if not student:
        print("No students found.")
        return
    
    print("\n Students Records:")
    for i, student in enumerate(students, start=1):
        print(f"Name: {student['name']}, Reg no: {student['reg_no']}Course: {student['course']}")

def search_student():
    reg_no = input("Enter Registration Number to search: ")
    found = False
    for student in students:
        if student['reg_no'] == reg_no:
            print(f"Found: Name: {student['name']}, Reg No: {student['reg_no']}, Course: {student['course']}")
            found = True
            break
        if not found:
            print("No student with such regisration number")  

def update_student():
    reg_no = input("Enter Registration number of student to update: ")
    for student in students:
        if student['reg_no'] == reg_no:
            print("Leave field blank to keep current value.")
            new_name = input(f"New name (current: {student['name']}): ") or student['name']
            new_course = input(f"New course (current: {student['course']})" )or student['course']

            student['name'] = new_name
            student['course'] = new_course
            print ("Student info updated.")
            return
        print("No student found with that registration number.")

def delete_student():
    reg_no = input("Enter registration number of student to delete: ")
    for i, student in enumerate(student):
     if student['reg_no'] == reg_no:
        confirm = input(f"Are you sure you want to delete {student['name']}? (y/n: ) ")
    if confirm.lower() == 'y':
        del students[i]
        print("Student deleted")
    else:
        print("Deletion cancelled")
        return
    print("No student found with such registration number")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    
    elif choice == '2':
        view_students()
        
    elif choice == '3':
        search_student()
        
    elif choice == '4':
        update_student()
    
    elif choice == '5':
        delete_student()
    
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break    
    else:
        print("Invalid choice. Try again.")    
"""

import json
import os
import getpass

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def admin_login():
    print("=====Admin Login=====")
    username = input("Username: ")
    password = getpass.getpass("password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Access denied.\n")
        return False

students = []
file_name = "students.json"

def load_data():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
              return []
        return[]
#save student file
def save_data():
    with open(file_name, 'w') as file:
        json.dump(students, file, indent=4)            
                

def show_menu():
    print("\n===== Student Record System =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Edit student")
    print("5. Delete student")
    print("6. Exit")

def add_student():
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "reg_no": reg_no,
        "course": course
    }

    students.append(student)
    print(f"✅ {name} added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent Records:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Reg No: {student['reg_no']}, Course: {student['course']}")

def search_student():
    reg_no = input("Enter Registration Number to search: ")
    found = False
    for student in students:
        if student['reg_no'] == reg_no:
            print(f"Found: Name: {student['name']}, Reg No: {student['reg_no']}, Course: {student['course']}")
            found = True
            break
    if not found:
        print("❌ No student found with that registration number.")

def update_student():
    reg_no = input("Enter Registration number of student to update: ")
    for student in students:
        if student['reg_no'] == reg_no:
            print("Leave field blank to keep current value.")
            new_name = input(f"New name (current: {student['name']}): ") or student['name']
            new_course = input(f"New course (current: {student['course']}): ") or student['course']

            student['name'] = new_name
            student['course'] = new_course
            print("✅ Student info updated.")
            return
    print("❌ No student found with that registration number.")

def delete_student():
    reg_no = input("Enter registration number of student to delete: ")
    for i, student in enumerate(students):
        if student['reg_no'] == reg_no:
            confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ")
            if confirm.lower() == 'y':
               del students[i]
               print("🗑 Student deleted.")
            else:
                print("❎ Deletion cancelled.")
            return
    print("❌ No student found with that registration number.")


#Main loop
if admin_login():
 while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("👋 Exiting program. Goodbye!")
        break
    else:
        exit()
    
