--CREATE TABLE students (
--    first_name TEXT,
--    last_name TEXT,
--    age INTEGER
--);
--
--CREATE TABLE employees (
--    first_name TEXT,
--    last_name TEXT,
--    age INTEGER
--);
--
--SELECT * FROM students;
--SELECT * FROM employees WHERE age IS 33;
--SELECT * FROM employees WHERE age > 19 AND age < 33;
--SELECT * FROM employees WHERE age BETWEEN 20 AND 30;
--SELECT * FROM employees WHERE age IS NOT 19;
--SELECT * FROM employees WHERE last_name LIKE "%k%";
--SELECT * FROM employees WHERE last_name LIKE "%en" OR first_name LIKE "Ma%";

--DROP TABLE employees;

--INSERT INTO employees (first_name, last_name, age) VALUES ("Aylin", "Gyoren", 27);
--INSERT INTO employees (first_name, last_name, age) VALUES ("Mary", "Nikolson", 19);
--INSERT INTO employees (first_name, last_name, age) VALUES ("Nick", "Ambruss", 21);
--INSERT INTO employees (first_name, last_name, age) VALUES ("Hue", "Jackman", 33);

--UPDATE employees SET first_name = "Nickie" WHERE last_name = "Ambruss";

--DELETE FROM employees WHERE first_name IS "Hue";

--DELETE FROM employees;