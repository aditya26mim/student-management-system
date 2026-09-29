# Student Record Management System

## Overview
A python based program for storing and managing data of a student, details like name , registratyion number , marks , percentage , subject , search and deletion of a students data

## Major Modules
1. Student Management - add, find, search and delete students.
2. Marks and Result Management - update marks and calculate total, percentage and pass/fail result.
3. Data Storage and Display - save records in JSON and display them in a readable format.

## Technologies
- Python 3
- JSON
- Git and GitHub
- VS Code

## Project Structure
```text
Student_Record_Management_System/
├── src/
│   ├── main.py
│   ├── student.py
│   ├── student_manager.py
│   ├── validator.py
│   ├── storage.py
│   ├── result.py
│   └── display.py
├── data/
│   └── students.json
├── tests/
│   └── test_system.py
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   ├── use_case.png
│   ├── sequence.png
│   ├── class_diagram.png
│   └── er_diagram.png
├── statement.md
└── README.md
```

## How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

python src/main.py
```

## Testing
Run:

python -m pytest

If pytest is not installed:

pip install pytest


## Data Storage
Student records are stored in `data/students.json`. No external database is required.

## Git Commands

git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
