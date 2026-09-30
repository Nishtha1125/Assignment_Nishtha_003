from fastapi import APIRouter, status
from app.models.student import Student
from app.controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# 1. CREATE
@router.post(
    "",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create(student: Student):
    return create_student(student)


# 2. READ ALL
@router.get(
    "",
    response_model=list[Student],
    status_code=status.HTTP_200_OK
)
def get_all():
    return get_all_students()


# 3. READ BY ID
@router.get(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_by_id(student_id: int):
    return get_student_by_id(student_id)


# 4. UPDATE
@router.put(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def update(student_id: int, student: Student):
    return update_student(student_id, student)


# 5. DELETE
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete(student_id: int):
    return delete_student(student_id)