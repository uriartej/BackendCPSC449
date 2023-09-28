class Course:
    def __init__(self, course_code, department, name):
        self.course_code = course_code
        self.department = department
        self.name = name


class Instructor:
    def __init__(self, instructor_id, name):
        self.instructor_id = instructor_id
        self.name = name


class ClassSection:
    def __init__(self, class_id, section_number, course_code, instructor_id, max_enrollment, current_enrollment=0, is_frozen=False):
        self.class_id = class_id
        self.section_number = section_number
        self.course_code = course_code
        self.instructor_id = instructor_id
        self.max_enrollment = max_enrollment
        self.current_enrollment = current_enrollment
        self.is_frozen = is_frozen


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Registration:
    def __init__(self, registration_id, class_id, student_id, status):
        self.registration_id = registration_id
        self.class_id = class_id
        self.student_id = student_id
        self.status = status


class WaitingList:
    def __init__(self, waiting_list_id, section_number, student_id, position, date_added):
        self.waiting_list_id = waiting_list_id
        self.section_number = section_number
        self.student_id = student_id
        self.position = position
        self.date_added = date_added
