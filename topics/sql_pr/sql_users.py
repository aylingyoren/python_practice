import sqlite3

conn = sqlite3.connect('users_db.db')
cursor = conn.cursor()

# create_table_query = ('CREATE TABLE users (name TEXT, pass TEXT)')
# cursor.execute(create_table_query)

users = [
    ("jane785034", "huhfifb885"),
    ("max6748", "njkc74bhj49")
]

# insert_query = "INSERT INTO users (name, pass) VALUES (?, ?)"
# cursor.executemany(insert_query, users)

user_name = input("Enter your username: ")
user_pass = input("Enter your password: ")

select_query = "SELECT * FROM users WHERE name = ? AND pass = ?"
cursor.execute(select_query, (user_name, user_pass))

# Prone to malicious injection
# select_query = f"SELECT * FROM users WHERE name = '{user_name}' AND pass = '{user_pass}'"
# cursor.execute(select_query)

data = cursor.fetchone()
if data:
    print("You are logged in")
else:
    print("Please try again.")

conn.commit()
conn.close()
