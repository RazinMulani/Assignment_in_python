# database.py
from pymongo import MongoClient
from config import MONGO_URI,DATABASE_NAME,collection_name

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[collection_name]

print("MongoDB Connected Successfully!")

# Insert Student Name
def insert_student(data):
    return collection.insert_one(data)

# Get all Students
def get_all_students():
    return collection.find()

# Search Student
def search_student(query):
    return collection.find(query)

# Find One Student
def find_student(student_id):
    return collecction.find_one({"student_id":student_id})

# Update Student
def update_student(student_id, new_data):
    return collectio.update_one(
        {"student_id":student_id},
        {"$set": new_data}
        )

# Delete Student
def delete_student(student_id):
    return collection.delete_one(
        {"student_id":student_id}
        )

# Count Students
def count_students():
    return collection.count_documents({})

# Close Connection
def close_connection():
    client.close()

def collection_drop():
    return collection.drop()
