CREATE TABLE users (
  user_id INT PRIMARY KEY,
  first VARCHAR(50),
  last VARCHAR(50),
  phone INT,
  email VARCHAR(100),
  password VARCHAR(50)
  is_manager BOOLEAN
);

CREATE TABLE competencies (
  competency_id INT PRIMARY KEY,
  competency_name VARCHAR(50),
  description TEXT
);

CREATE TABLE assessments (
  assessment_id INT PRIMARY KEY,
  assessment_name VARCHAR(50),
  description TEXT,
  competency_id INT,
  FOREIGN KEY (competency_id) REFERENCES competencies(competency_id)
);

CREATE TABLE assessment_results (
  result_id INT PRIMARY KEY,
  user_id INT,
  assessment_id INT,
  score FLOAT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id)
);