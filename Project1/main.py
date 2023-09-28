import sqlite3
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from typing import List
import crud, schemas
import urllib.parse

database_file_path = "/home/juanuriarte/Project1/Updated Database Project 1.db"

encoded_file_path = urllib.parse.quote(database_file_path, safe = "/:")
DATABASE_URL = f"sqlite:///{encoded_file_path}"
app = FastAPI()

# Dependency to get the database session
def get_db():
    conn = sqlite3.connect(database_file_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>FastAPI Routes</title>
        </head>
        <body>
            <h1>List of Routes:</h1>
            <ul>
                <li><b>POST</b> /instructors/ - Create a new instructor</li>
                <li><b>GET</b> /instructors/ - Read instructors</li>
                <li><b>GET</b> /instructors/{instructor_id} - Read an instructor by ID</li>
                <li><b>POST</b> /class_sections/ - Create a new class section</li>
                <li><b>GET</b> /class_sections/ - Read class sections</li>
                <li><b>GET</b> /class_sections/{class_id} - Read a class section by ID</li>
                <li><b>POST</b> /students/ - Create a new student</li>
                <li><b>GET</b> /students/ - Read students</li>
                <li><b>GET</b> /students/{student_id} - Read a student by ID</li>
                <li><b>POST</b> /registrations/ - Create a new registration</li>
                <li><b>GET</b> /registrations/ - Read registrations</li>
                <li><b>GET</b> /registrations/{registration_id} - Read a registration by ID</li>
                <li><b>POST</b> /waiting_lists/ - Create a new waiting list</li>
                <li><b>GET</b> /waiting_lists/ - Read waiting lists</li>
                <li><b>GET</b> /waiting_lists/{waiting_list_id} - Read a waiting list by ID</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Instructor Routes
@app.post("/instructors/", response_model=schemas.Instructor)
def create_instructor(instructor: schemas.InstructorCreate, conn = Depends(get_db), ):
    instructor_id = crud.create_instructor(conn = conn, instructor = instructor)
    conn.commit()
    return crud.get_instructor_by_id(conn, instructor_id = instructor_id)

@app.get("/instructors/", response_model=List[schemas.Instructor])
def read_instructors(skip: int = 0, limit: int = 10, conn = Depends(get_db)):
    return crud.get_instructors(conn, skip=skip, limit=limit)

@app.get("/instructors/{instructor_id}", response_model=schemas.Instructor)
def read_instructor(instructor_id: int, conn = Depends(get_db)):
    db_instructor = crud.get_instructor_by_id(conn, instructor_id=instructor_id)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return db_instructor


# ClassSection Routes
@app.post("/class_sections/", response_model=schemas.ClassSection)
def create_class_section(conn, class_section: schemas.ClassSectionCreate):
    class_id = crud.create_class_section(conn = conn, class_section = class_section)
    conn.commit()
    return crud.get_class_section_by_id(conn, class_id = class_id)

@app.get("/class_sections/", response_model=List[schemas.ClassSection])
def read_class_sections(skip: int = 0, limit: int = 10, conn = Depends(get_db)):
    return crud.get_class_sections(conn, skip=skip, limit=limit)

@app.get("/class_sections/{class_id}", response_model=schemas.ClassSection)
def read_class_section(class_id: int, conn = Depends(get_db)):
    db_class_section = crud.get_class_section_by_id(conn, class_id=class_id)
    if db_class_section is None:
        raise HTTPException(status_code=404, detail="ClassSection not found")
    return db_class_section


# Student Routes
@app.post("/students/", response_model=schemas.Student)
def create_student(conn, student: schemas.StudentCreate):
    student_id = crud.create_student(conn = conn, student = student)
    conn.commit()
    return crud.get_student_by_id(conn = conn, student_id = student_id)

@app.get("/students/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, conn = Depends(get_db)):
    return crud.get_students(conn, skip=skip, limit=limit)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, conn = Depends(get_db)):
    db_student = crud.get_student_by_id(conn, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# Registration Routes
@app.post("/registrations/", response_model=schemas.Registration)
def create_registration(conn, registration: schemas.RegistrationCreate):
    registration_id = crud.create_registration(conn = conn, registration = registration)
    conn.commit()
    return crud.get_registration_by_id(conn, registration_id = registration_id)

@app.get("/registrations/", response_model=List[schemas.Registration])
def read_registrations(skip: int = 0, limit: int = 10, conn = Depends(get_db)):
    return crud.get_registrations(conn, skip=skip, limit=limit)

@app.get("/registrations/{registration_id}", response_model=schemas.Registration)
def read_registration(registration_id: int, conn = Depends(get_db)):
    db_registration = crud.get_registration_by_id(conn, registration_id=registration_id)
    if db_registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")
    return db_registration


# WaitingList Routes
@app.post("/waiting_lists/", response_model=schemas.WaitingList)
def create_waiting_list(conn, waiting_list: schemas.WaitingListCreate):
    waiting_list_id = crud.create_waiting_list(conn = conn, waiting_list = waiting_list)
    conn.commit()
    return crud.get_waiting_list_by_id(conn, waiting_list_id = waiting_list_id)

@app.get("/waiting_lists/", response_model=List[schemas.WaitingList])
def read_waiting_lists(skip: int = 0, limit: int = 10, conn = Depends(get_db)):
    return crud.get_waiting_lists(conn, skip=skip, limit=limit)



@app.get("/waiting_lists/{waiting_list_id}", response_model=schemas.WaitingList)
def read_waiting_list(conn, waiting_list_id: int):
    db_waiting_list = crud.get_waiting_list_by_id(conn, waiting_list_id=waiting_list_id)
    if db_waiting_list is None:
        raise HTTPException(status_code=404, detail="WaitingList not found")
    return db_waiting_list
