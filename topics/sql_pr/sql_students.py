import sqlite3


# def show_earthquakes():
#     conn = sqlite3.connect('../../apps/earthquakes_db.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM earthquakes')
#     [print(eq) for eq in cursor.fetchall()]
#
#     conn.commit()
#     conn.close()
#
#
# show_earthquakes()

# conn = sqlite3.connect('students_db.db')
# cursor = conn.cursor()
#
# # cursor.execute("""
# # CREATE TABLE students (
# #     first_name TEXT,
# #     last_name TEXT,
# #     age INTEGER
# # );
# # """)
#
# first_name = "Bob"
# last_name = "Marley"
# age = 38
#
# kate_tuple = ("Kate", "Lewis", 30)
# students = [
#     ("Nate", "Jacobs", 17),
#     ("Maddy", "Gomez", 17)
# ]
#
# students1 = [
#     ("Rue", "Zendaya", 17),
#     ("Jules", "Hunter", 17)
# ]
#
# insert_query = "INSERT INTO students (first_name, last_name, age) VALUES (?, ?, ?);"

# for student in students1:
#     cursor.execute(insert_query, student)

# cursor.execute(insert_query, (first_name, last_name, age))

# cursor.execute("""
# INSERT INTO students (first_name, last_name, age) VALUES ("Freddy", "Davidson", 20);
# """)

# cursor.execute(insert_query, kate_tuple)
# cursor.executemany(insert_query, students)

# cursor.execute('UPDATE students SET last_name = "Lopez" WHERE first_name = "Maddy"')

# cursor.execute('DELETE FROM students WHERE first_name = "Nate"')
# cursor.execute('DELETE FROM students WHERE first_name = "Maddy"')
# cursor.execute('DELETE FROM students WHERE first_name = "Rue"')
# cursor.execute('DELETE FROM students WHERE first_name = "Jules"')

# cursor.execute('SELECT * FROM students;')
# for student in cursor:
#     print(student)
#
# conn.commit()
# conn.close()
