CREATE TABLE Users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first VARCHAR(50),
  last VARCHAR(50),
  phone TEXT,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(50),
  is_manager INTEGER DEFAULT 0,
  active INTEGER DEFAULT 1
);

CREATE TABLE Competencies (
  competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
  competency_name VARCHAR(50),
  date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Assessments (
  assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  competency_id INTEGER NOT NULL,
  result INTEGER,
  date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (competency_id) REFERENCES competencies(competency_id)
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO Users (first, last, phone, email, password, is_manager) 
VALUES("dan", "blonquist", "5555555555", "dan@dan.com", "coolcool", 1),
("Jack", "Jill", "5555555554", "jack@jill.com", 'password', 0);

INSERT INTO Competencies (competency_name)
VALUES('Data Types'),
('Variables'),
('Functions'),
('Boolean Logic'),
('Conditionals'),
('Loops'),
('Data Structures'),
('Lists'),
('Dictionaries'),
('Working with Files'),
('Exception Handling'),
('Quality Assurance (QA)'),
('Object-Oriented Programming'),
('Recursion'),
('Databases');

INSERT INTO Assessments (user_id, competency_id, result)
VALUES (1, 1, 2),
(2,1,4);