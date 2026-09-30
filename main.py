from fastapi import FastAPI, Depends 
from model import Student, Enrollment, Instructor, Course
from database import engine, Base, SessionLocal
from sqlalchemy.orm import Session
from schemas import StudentCreate, StudentUpdate, InstructorCreate, InstructorUpdate, CreateCourse, UpdateCourse, CreateEnrollment, UpdateEnrollment


Base.metadata.create_all(bind = engine)

app = FastAPI(redirect_slashes=False)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get('/')
def home():
    return {"Hello" : "A welcome message"}

# ---------------------------------------------------------------------------------------Student
@app.get("/students")
def get_stu(db : Session = Depends(get_db)):
    students = db.query(Student).all()
    return students
    
@app.post("/students")
def create_student(student : StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        name = student.name,
        age = student.age,
        email = student.email,
        ph_no = student.ph_no
    )

    db.add(new_student)
    db.commit()

    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    old_student = db.query(Student).filter(Student.id == student_id).first()

    old_student.name = student.name
    old_student.age = student.age
    old_student.email = student.email
    old_student.ph_no = student.ph_no

    db.commit()
    db.refresh(old_student)

    return old_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    del_student = db.query(Student).filter(Student.id == student_id).first()

    db.delete(del_student)
    db.commit()

    return {"Student" : "No data"}

# ----------------------------------------------------------------------------------------------------------Instructor

@app.get("/instructors")
def get_instructor(db : Session = Depends(get_db)):
    instructors = db.query(Instructor).all()
    return instructors

@app.post("/instructors")
def create_instructor(instructor : InstructorCreate, db : Session = Depends(get_db)):

    new_instructor = Instructor(
        name = instructor.name,
        email = instructor.email
    )

    db.add(new_instructor)
    db.commit()

    return new_instructor

@app.put("/instructors/{instructor_id}")
def update_instructor(instructor_id: int, instructor: InstructorUpdate, db: Session = Depends(get_db)):
    db_instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    

    db_instructor.name = instructor.name
    db_instructor.email = instructor.email

    db.commit()
    db.refresh(db_instructor)

    return db_instructor

@app.delete("/instructors/{instructor_id}")
def delete_instructor(instructor_id:int,  db: Session = Depends(get_db)):
    del_instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()

    db.delete(del_instructor)
    db.commit()

    return {"msg" : "successfully deleted"}

# ---------------------------------------------------------------------------------------------------Courses

@app.get("/courses")
def get_courses(db : Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses

@app.post("/courses")
def create_course(course : CreateCourse, db: Session = Depends(get_db)):

    new_course = Course(
        name = course.name,
        description = course.description,
        instructor_id = course.instructor_id
    )

    db.add(new_course)
    db.commit()

    return new_course

@app.put("/courses/{course_id}")
def update_course(course_id : int, course : UpdateCourse, db: Session = Depends(get_db)):
    old_course = db.query(Course).filter(Course.id == course_id).first()

    old_course.name = course.name,
    old_course.description = course.description
    old_course.instructor_id = course.instructor_id

    db.commit()
    db.refresh(old_course)

    return old_course

@app.delete("/courses/{course_id}")
def delete_course(course_id : int, db : Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()

    db.delete(db_course)
    db.commit()

    return {'msg' : "Deleted successfully"}


# ---------------------------------------------------------------------------------------------------Enrollment

@app.get("/enrollment")
def get_enrollments(db: Session = Depends(get_db)):
    enrollment = db.query(Enrollment).all
    return enrollment

@app.post("/enrollment")
def create_enrollment(enrollment : CreateEnrollment, db: Session = Depends(get_db)):

    new_enrollment = Enrollment(
        student_id = new_enrollment.student_id,
        course_id = new_enrollment.course_id
    )

    db.add(new_enrollment)
    db.commit()

    return new_enrollment

@app.put("/enrollment/{enroll_id}")
def update_enrollment(enroll_id : int, enrollment : UpdateEnrollment, db: Session = Depends(get_db)):
    old_enroll = db.query(Enrollment).filter(Enrollment.id == enroll_id).first()

    old_enroll.student_id = enrollment.student_id
    old_enroll.course_id = enrollment.course_id

    db.commit()
    db.refresh(old_enroll)

    return old_enroll


@app.delete("/enrollment/{enroll_id}")
def delete_enrollment(enroll_id : int, db: Session = Depends(get_db)):
    db_enroll = db.query(Enrollment).filter(Enrollment.id == enroll_id).first()

    db.delete(db_enroll)
    db.commit()

    return {"msg" : "Deleted Successfully"}