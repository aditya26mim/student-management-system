
class Student:
    def __init__(self, student_id, name, age, course, marks=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks if marks else {}

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        if not self.marks:
            return 0
        return self.calculate_total() / len(self.marks)

    def get_result(self):
        if not self.marks:
            return "Marks Not Entered"
        if any(mark < 40 for mark in self.marks.values()):
            return "Fail"
        return "Pass"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data.get("marks", {})
        )
