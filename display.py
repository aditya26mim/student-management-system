
class Student:
    def __init__(self, student_id, name, age, course, marks=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

def print_student(student):
    print("-" * 50)
    print(f"ID      : {student.student_id}")
    print(f"Name    : {student.name}")
    print(f"Age     : {student.age}")
    print(f"Course  : {student.course}")
    print(f"Marks   : {student.marks if student.marks else 'Not entered'}")
    print("-" * 50)

def print_students(students):
    if not students:
        print("No student records found.")
        return
    for student in students:
        print_student(student)

if __name__ == "__main__":
    student1 = Student("S001 , Aditya jamliya ", 20, "Computer Science", 88)
    student2 = Student("S002", "abhishek ", 22, "Mathematics")
    print_students([student1, student2])
