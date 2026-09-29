
import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "students.json"

def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [Student.from_dict(item) for item in data]
    except (json.JSONDecodeError, OSError):
        return []

def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)
