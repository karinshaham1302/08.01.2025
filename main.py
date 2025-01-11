import sqlitelib
import os

db_name: str = "08_01_2025.db"
conn, cursor = sqlitelib.connect_db(db_name)

course_name = input('Enter new course name:')
course_hours = float(input('Enter course hours:'))

sqlitelib.update_query(
    cursor, conn,
    "INSERT INTO courses (topic, hours) VALUES (?, ?)",
    (course_name, course_hours))

result_select_courses = sqlitelib.read_query(cursor, "SELECT * from courses")
for courses in result_select_courses:
    print(courses)

if os.path.exists(db_name):
    os.remove(db_name)
    print(f"Database file '{db_name}' was deleted.")
else:
    print(f"Database file '{db_name}' does not exist.")

conn.close()
