from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

store_id = db.stores.find_one({"name": "Магазин на Рекордной"})["_id"]
print(store_id)

pipeline = [
    {
        "$match": {
            "store_id": store_id
        }
    },
    {
        "$project": {
            "products": 1
        }
    }

]

result = db.stock_balances.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)
