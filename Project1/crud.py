import sqlite3
from typing import List, Optional, Dict, Any, Tuple

conn = sqlite3.connect('Updated_Database_Project1.db')
cursor = conn.cursor()

# CRUD for Course
def get_courses(conn: sqlite3.Connection, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM course LIMIT {limit} OFFSET {skip}')
    rows = cursor.fetchall()
    return [dict(zip(('course_code', 'course_name'), row)) for row in rows]

def get_course_by_code(conn: sqlite3.Connection, course_code: str) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM course WHERE course_code = ?', (course_code,))
    row = cursor.fetchone()
    return dict(zip(('course_code', 'course_name'), row)) if row else None

def create_course(conn: sqlite3.Connection, course_data: Tuple[Any, ...]) -> Dict[str, Any]:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO course (course_code, course_name) VALUES (?, ?)', course_data)
    conn.commit()
    return dict(zip(('course_code', 'course_name'), course_data))

# CRUD for Instructor
def get_instructors(conn: sqlite3.Connection, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM instructor LIMIT {limit} OFFSET {skip}')
    rows = cursor.fetchall()
    return [dict(zip(('instructor_id', 'name', 'email'), row)) for row in rows]

def get_instructor_by_id(conn: sqlite3.Connection, instructor_id: int) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM instructor WHERE instructor_id = ?', (instructor_id,))
    row = cursor.fetchone()
    return dict(zip(('instructor_id', 'name', 'email'), row)) if row else None

def create_instructor(conn: sqlite3.Connection, name: str, email: str) -> Dict[str, Any]:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO instructor (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    instructor_id = cursor.lastrowid
    return {'instructor_id': instructor_id, 'name': name, 'email': email}


# CRUD for ClassSection
def get_class_sections(conn: sqlite3.Connection, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM class_section LIMIT {limit} OFFSET {skip}')
    rows = cursor.fetchall()
    return [dict(zip(('class_id', 'class_name', 'instructor_id', 'schedule'), row)) for row in rows]

def get_class_section_by_id(conn: sqlite3.Connection, class_id: int) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM class_section WHERE class_id = ?', (class_id,))
    row = cursor.fetchone()
    return dict(zip(('class_id', 'class_name', 'instructor_id', 'schedule'), row)) if row else None

def create_class_section(conn: sqlite3.Connection, class_name: str, instructor_id: int, schedule: str) -> Dict[str, Any]:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO class_section (class_name, instructor_id, schedule) VALUES (?, ?, ?)', (class_name, instructor_id, schedule))
    conn.commit()
    class_id = cursor.lastrowid
    return {'class_id': class_id, 'class_name': class_name, 'instructor_id': instructor_id, 'schedule': schedule}


# CRUD for Student
def get_students(conn: sqlite3.Connection, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM student LIMIT {limit} OFFSET {skip}')
    rows = cursor.fetchall()
    return [dict(zip(('student_id', 'first_name', 'last_name', 'email'), row)) for row in rows]

def get_student_by_id(conn: sqlite3.Connection, student_id: int) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student WHERE student_id = ?', (student_id,))
    row = cursor.fetchone()
    return dict(zip(('student_id', 'first_name', 'last_name', 'email'), row)) if row else None

def create_student(conn: sqlite3.Connection, first_name: str, last_name: str, email: str) -> Dict[str, Any]:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student (first_name, last_name, email) VALUES (?, ?, ?)', (first_name, last_name, email))
    conn.commit()
    student_id = cursor.lastrowid
    return {'student_id': student_id, 'first_name': first_name, 'last_name': last_name, 'email': email}

# CRUD for Registration
def get_registrations(conn: sqlite3.Connection, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM registration LIMIT {limit} OFFSET {skip}')
    rows = cursor.fetchall()
    return [dict(zip(('registration_id', 'student_id', 'class_id', 'registration_date'), row)) for row in rows]

def get_registration_by_id(conn: sqlite3.Connection, registration_id: int) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registration WHERE registration_id = ?', (registration_id,))
    row = cursor.fetchone()
    return dict(zip(('registration_id', 'student_id', 'class_id', 'registration_date'), row)) if row else None

def create_registration(conn: sqlite3.Connection, student_id: int, class_id: int, registration_date: str) -> Dict[str, Any]:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO registration (student_id, class_id, registration_date) VALUES (?, ?, ?)', (student_id, class_id, registration_date))
    conn.commit()
    registration_id = cursor.lastrowid
    return {'registration_id': registration_id, 'student_id': student_id, 'class_id': class_id, 'registration_date': registration_date}

# CRUD for WaitingList
def get_waiting_lists(conn: sqlite3.Connection, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM waiting_list LIMIT {limit} OFFSET {skip}')
    rows = cursor.fetchall()
    return [dict(zip(('waiting_list_id', 'student_id', 'class_id', 'timestamp'), row)) for row in rows]

def get_waiting_list_by_id(conn: sqlite3.Connection, waiting_list_id: int) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM waiting_list WHERE waiting_list_id = ?', (waiting_list_id,))
    row = cursor.fetchone()
    return dict(zip(('waiting_list_id', 'student_id', 'class_id', 'timestamp'), row)) if row else None

def create_waiting_list(conn: sqlite3.Connection, student_id: int, class_id: int, timestamp: str) -> Dict[str, Any]:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO waiting_list (student_id, class_id, timestamp) VALUES (?, ?, ?)', (student_id, class_id, timestamp))
    conn.commit()
    waiting_list_id = cursor.lastrowid
    return {'waiting_list_id': waiting_list_id, 'student_id': student_id, 'class_id': class_id, 'timestamp': timestamp}

