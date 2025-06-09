from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

from InsertSales import employee_id

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

pipeline = [
    {
        "$match": {
            "name": "Универмаг на Соборной"
        }
    },
    {
        "$unwind": "$employees"
    },
    {
        "$lookup": {
            "from": "employees",
            "localField": "employees",
            "foreignField": "_id",
            "as": "employee",
        }
    },
    {
        "$project": {
            "employee.salary": 1
        }
    }
]

result = db.stores.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)


