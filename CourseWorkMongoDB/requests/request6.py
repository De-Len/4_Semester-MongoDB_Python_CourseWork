from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]


product_id = db.products.find_one({
    "name": "Чайник 'Гарри'",
})["_id"]
# print(product_id)

# указанного типа
stores_cursor = db.stores.find({"type": "Универмаг"})
stores_id = [store["_id"] for store in stores_cursor]
# print(stores_id)

start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 5, 31, 23, 59, 59)

match_stage = {
    "$match": {
        "date": {
            "$gte": start_date,
            "$lte": end_date
        },
        "store_id": {"$in": stores_id},
        "product_id": product_id
    }
}

pipeline = [
    match_stage,
    {
        "$group": {
            "_id": None,  # Все документы в одну группу
            "total_quantity": {"$sum": "$quantity"}
        }
    }
]

result = db.sales.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)


