from typing import List, Optional
from pydantic import BaseModel

# Course Models
class CourseBase(BaseModel):
    course_code: str
    department: str
    name: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    pass


# Instructor Models
class InstructorBase(BaseModel):
    name: str

class InstructorCreate(InstructorBase):
    pass

class Instructor(InstructorBase):
    instructor_id: int


# ClassSection Models
class ClassSectionBase(BaseModel):
    section_number: str
    course_code: str
    instructor_id: int
    max_enrollment: int
    current_enrollment: int
    is_frozen: bool

class ClassSectionCreate(ClassSectionBase):
    pass

class ClassSection(ClassSectionBase):
    class_id: int


# Student Models
class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int


# Registration Models
class RegistrationBase(BaseModel):
    class_id: int
    student_id: int
    status: str

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    registration_id: int


# WaitingList Models
class WaitingListBase(BaseModel):
    section_number: str
    student_id: int
    position: int
    date_added: str

class WaitingListCreate(WaitingListBase):
    pass

class WaitingList(WaitingListBase):
    waiting_list_id: int

