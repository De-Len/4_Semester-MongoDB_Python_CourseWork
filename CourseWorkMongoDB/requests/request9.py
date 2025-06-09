from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

# номер заказа - его id
pipeline = [
    {
        "$match": {
            "_id": ObjectId("6846754141f00dde3bb185d3"),

        }
    }
]

result = db.supply_orders.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)
