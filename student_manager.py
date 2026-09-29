
from student import Student
from validator import validate_student_id, validate_name, validate_age, validate_marks

class StudentManager:
    def __init__(self, students=None):
        self.students = students if students is not None else []

    def add_student(self, student_id, name, age, course):
        if not validate_student_id(student_id):
            return False, "Student ID cannot be empty."
        if self.find_student(student_id):
            return False, "Student ID already exists."
        if not validate_name(name):
            return False, "Name must contain letters and spaces only."
        if not validate_age(age):
            return False, "Age must be between 15 and 100."
        self.students.append(Student(student_id, name, age, course))
        return True, "Student added successfully."

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student
        return None

    def search_students(self, keyword):
        keyword = keyword.lower()
        return [
            s for s in self.students
            if keyword in s.student_id.lower()
            or keyword in s.name.lower()
            or keyword in s.course.lower()
        ]

    def update_marks(self, student_id, subject, mark):
        student = self.find_student(student_id)
        if not student:
            return False, "Student not found."
        if not validate_marks(mark):
            return False, "Marks must be between 0 and 100."
        student.marks[subject] = mark
        return True, "Marks updated successfully."

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return False, "Student not found."
        self.students.remove(student)
        return True, "Student deleted successfully."
