
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from storage import load_students, save_students
from student_manager import StudentManager
from result import format_result
from display import print_students

def show_menu():
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Calculate Total / Percentage / Result")
    print("5. Display All Students")
    print("6. Delete Student")
    print("7. Exit")

def main():
    manager = StudentManager(load_students())

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Invalid age.")
                continue
            course = input("Enter course: ").strip()
            ok, message = manager.add_student(student_id, name, age, course)
            print(message)
            if ok:
                save_students(manager.students)

        elif choice == "2":
            keyword = input("Enter ID, name, or course to search: ").strip()
            print_students(manager.search_students(keyword))

        elif choice == "3":
            student_id = input("Enter student ID: ").strip()
            subject = input("Enter subject: ").strip()
            try:
                mark = float(input("Enter marks (0-100): "))
            except ValueError:
                print("Invalid marks.")
                continue
            ok, message = manager.update_marks(student_id, subject, mark)
            print(message)
            if ok:
                save_students(manager.students)

        elif choice == "4":
            student_id = input("Enter student ID: ").strip()
            student = manager.find_student(student_id)
            if student:
                print("\n" + format_result(student))
            else:
                print("Student not found.")

        elif choice == "5":
            print_students(manager.students)

        elif choice == "6":
            student_id = input("Enter student ID: ").strip()
            ok, message = manager.delete_student(student_id)
            print(message)
            if ok:
                save_students(manager.students)

        elif choice == "7":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
