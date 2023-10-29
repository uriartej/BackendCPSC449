INSERT INTO users (username, first_name, last_name) VALUES
('alice', 'Alice', 'Smith'),
('bob', 'Bob', 'Jones'),
('carol', 'Carol', 'Williams'),
('dave', 'Dave', 'Brown'),
('eve', 'Eve', 'Johnson'),
('frank', 'Frank', 'Miller'),
('grace', 'Grace', 'Davis'),
('harry', 'Harry', 'Wilson'),
('isabel', 'Isabel', 'Taylor'),
('jack', 'Jack', 'Garcia'),
('kim', 'Kim', 'Martinez'),
('larry', 'Larry', 'Anderson'),
('mary', 'Mary', 'Lopez'),
('nick', 'Nick', 'Robinson'),
('olivia', 'Olivia', 'Walker'),
('peter', 'Peter', 'Perez'),
('qiana', 'Qiana', 'Johnson'),
('robert', 'Robert', 'Brown'),
('sarah', 'Sarah', 'Davis'),
('thomas', 'Thomas', 'Miller'),
('ursula', 'Ursula', 'Wilson');

INSERT INTO departments VALUES
(1, 'Computer Science'),
(2, 'Engineering'),
(3, 'Mathematics');

INSERT INTO courses VALUES
(1, 'CPSC 449', 'Web Back-End Engineering', 1),
(2, 'MATH 150A', 'Calculus I', 3);

INSERT INTO sections VALUES
(1, 1, 'CS102', 30, 15, 'Tuesday', '7pm', '9:45pm', 2, 0, 0),
(2, 1, 'CS104', 30, 15, 'Wednesday', '4pm', '6:45pm', 2, 0, 0),
(3, 2, 'MH302', 35, 15, 'Monday', '12pm', '2:45pm', 4, 0, 0),
(4, 2, 'MH107', 32, 15, 'Thursday', '9am', '11:30am', 4, 0, 0);

INSERT INTO enrollments VALUES
(5, 1, 'Enrolled', NULL, '2023-09-15'),
(6, 1, 'Enrolled', NULL, '2023-09-15'),
(7, 1, 'Enrolled', NULL, '2023-09-15'),
(8, 1, 'Enrolled', NULL, '2023-09-15'),
(9, 2, 'Enrolled', NULL, '2023-09-15'),
(10, 2, 'Dropped', NULL, '2023-09-15'),
(11, 2, 'Enrolled', NULL, '2023-09-15'),
(12, 3, 'Enrolled', NULL, '2023-09-15'),
(13, 3, 'Dropped', NULL, '2023-09-15'),
(14, 4, 'Enrolled', NULL, '2023-09-15'),
(5, 3, 'Enrolled', NULL, '2023-09-15'),
(6, 4, 'Enrolled', NULL, '2023-09-15'),
(7, 2, 'Enrolled', NULL, '2023-09-15');

-- For waitlist table
INSERT INTO waitlist VALUES
(8, 3, 1, '2023-09-15'),
(9, 2, 1, '2023-09-15'),
(10, 4, 2, '2023-09-15'),
(11, 1, 2, '2023-09-15'),
(12, 3, 3, '2023-09-15'),
(13, 1, 3, '2023-09-15'),
(14, 2, 4, '2023-09-15');
