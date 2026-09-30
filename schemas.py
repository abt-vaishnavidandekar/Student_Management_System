from pydantic import BaseModel, EmailStr 

class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr 
    ph_no: str

class StudentUpdate(BaseModel):
    name: str
    age: int
    email: EmailStr
    ph_no: str

    class Config:
        from_attributes = True

class InstructorCreate(BaseModel):
    name : str
    email : EmailStr

class InstructorUpdate(BaseModel):
    name : str
    email : EmailStr

    class Config:
        from_attributes = True

class CreateCourse(BaseModel):
    name : str
    description : str
    instructor_id : int

class UpdateCourse(BaseModel):
    name : str
    description : str
    instructor_id : int

    class Config:
        from_attributes = True

class CreateEnrollment(BaseModel):
    student_id : int
    course_id : int


class UpdateEnrollment(BaseModel):
    student_id : int
    course_id : int

    class Config:
        from_attributes = True


