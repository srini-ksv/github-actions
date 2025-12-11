CREATE DATABASE appdb;
\c appdb;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(50)
);

INSERT INTO students (name, course)
VALUES ('Alice', 'Docker Basics'), ('Bob', 'DevOps Mastery');