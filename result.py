
def get_result_details(student):
    total = student.calculate_total()
    percentage = student.calculate_percentage()
    result = student.get_result()
    return {
        "total": total,
        "percentage": percentage,
        "result": result
    }

def format_result(student):
    details = get_result_details(student)
    lines = [
        f"Student ID : {student.student_id}",
        f"Name       : {student.name}",
        f"Course     : {student.course}",
        f"Marks      : {student.marks}",
        f"Total      : {details['total']}",
        f"Percentage : {details['percentage']:.2f}%",
        f"Result     : {details['result']}"
    ]
    return "\n".join(lines)
