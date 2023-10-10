import sqlite3
import datetime

def create_database():
    conn = sqlite3.connect("project1.db")  
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Instructors (
            InstructorId INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT,
            Email TEXT
        )
    ''')
    conn.execute("insert into Instructors(FirstName,LastName,Email) values('Mike','Garcia','MikeGarcia@gmail.com');")
    conn.execute("insert into Instructors(FirstName,LastName,Email) values('Denise','Jones','DeniseJones@gmail.com');")
    conn.execute("insert into Instructors(FirstName,LastName,Email) values('Zack','Smith','ZackSmith@gmail.com');")


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Classes (
            ClassId INTEGER PRIMARY KEY,
            InstructorId INT REFERENCES Instructors(InstructorId),
            Department TEXT,
            CourseCode TEXT,
            SectionNumber INTEGER,
            ClassName TEXT,
            CurrentEnrollment INTEGER,
            MaxEnrollment INTEGER,
            AutomaticEnrollmentFrozen INTEGER DEFAULT 0
        )
    ''')
    conn.execute("insert into Classes(Department,CourseCode,SectionNumber,ClassName,InstructorID,\
                 CurrentEnrollment,MaxEnrollment) values('Computer Science','CPSC351',1,\
                 'Operating Systems',5,30,45);")
    conn.execute("insert into Classes(Department,CourseCode,SectionNumber,ClassName,InstructorID,\
                 CurrentEnrollment,MaxEnrollment) values('Computer Science','CPSC240',2,\
                 'Assembly',4,23,30);")
    conn.execute("insert into Classes(Department,CourseCode,SectionNumber,ClassName,InstructorID,\
                 CurrentEnrollment,MaxEnrollment) values('Computer Science','CPSC223',3,\
                 'Python',3,30,35);")
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentId INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT,
            Email TEXT
        )
    ''')
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_1','LastName_1','abc1@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_2','LastName_2','abc2@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_3','LastName_3','abc3@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_4','LastName_4','abc4@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_5','LastName_5','abc5@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_6','LastName_6','abc6@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_7','LastName_7','abc7@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_8','LastName_8','abc8@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_9','LastName_9','abc9@gmail.com');")
    conn.execute("insert into Students(FirstName,LastName,Email) values('FirstName_10','LastName_10','abc10@gmail.com');")


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Enrollments (
            EnrollmentId INTEGER PRIMARY KEY,
            StudentId INT REFERENCES Students(StudentId),
            ClassId INT REFERENCES Classes(ClassId),
            EnrollmentDate TEXT,
            Dropped INT DEFAULT 0
        )
    ''')
    
    # conn.execute("insert into Enrollments(StudentID,ClassID,EnrollmentDate) values(1,1,datetime('now'));",)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WaitingLists (
            WaitListId INTEGER PRIMARY KEY,
            StudentId INT REFERENCES Students(StudentId),
            ClassId INT REFERENCES Classes(ClassId),
            WaitingListPos INT,
            DateAdded TEXT
        )
    ''')
    
    # conn.execute("insert into waitingLists(StudentID,ClassID,WaitingListPos,DateAdded) values(1,1,1,datetime('now'));",)

    

    conn.commit()
    conn.close()

create_database()


# conn = sqlite3.connect("pro1.db")  
# cursor = conn.cursor()
# conn.execute("insert into Classes(Department,CourseCode,SectionNumber,ClassName,InstructorID,\
#               CurrentEnrollment,MaxEnrollment) values('Computer Science','CPSC541',1,\
#             'Advance Software Process',2,40,40);")
# conn.commit()
# conn.close()