# test_database.py

from database import *

student = {
    "student_id":1,
    "name":"Razin",
    "age":22
    }

#insert_student(student)


delete_student({"student_id":1})
print("delete")

print(count_students())
print("count0")
print(collection_drop())
#print(count_students())
for data in get_all_students():
    print(data)

