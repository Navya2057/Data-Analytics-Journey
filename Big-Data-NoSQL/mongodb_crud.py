from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
collection = db["employees"]

collection.insert_one({
    "name": "Rahul",
    "department": "IT",
    "salary": 50000
})

print("Inserted Successfully")

for employee in collection.find():
    print(employee)

collection.update_one(
    {"name": "Rahul"},
    {"$set": {"salary": 55000}}
)

collection.delete_one({"name": "Rahul"})

print("CRUD Operations Completed")
