from pydantic import BaseModel, Field, EmailStr


class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    age: int = Field(..., ge=17, le=60)
    course: str = Field(..., min_length=2)
    email: EmailStr