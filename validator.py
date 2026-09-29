
from webbrowser import get


def validate_student_id(student_id):
    return bool(student_id.strip())

def validate_name(name):
    return bool(name.strip()) and all(ch.isalpha() or ch.isspace() for ch in name)

def validate_age(age):
    return 15 <= age <= 100

def validate_marks(mark):
    return 0 <= mark <= 100
