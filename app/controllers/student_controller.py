from fastapi import HTTPException
from app.models.student import Student


students = {}


# CREATE
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(
            status_code=409,
            detail="Student with this ID already exists"
        )

    students[student.id] = student
    return student


def get_all_students():
    return list(students.values())


def get_student_by_id(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


# UPDATE
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if student.id != student_id:
        raise HTTPException(
            status_code=400,
            detail="Student ID in body must match URL ID"
        )

    students[student_id] = student
    return student


# DELETE
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }