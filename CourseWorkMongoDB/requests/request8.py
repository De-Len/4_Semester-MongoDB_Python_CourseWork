from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 5, 31, 23, 59, 59)

match_date_stage = {
    "$match": {
        "date": {
            "$gte": start_date,
            "$lte": end_date
        }
    }
}

# обязательно указывать какого поставщика
product_id = db.products.find_one({
    "name": "Футболка 'I Am Groot'",
    "supplier_id": ObjectId("665f1100a1a1a1a1a1a1a201")
})["_id"]
print(product_id)

# попались без фиксированных покупателей, поэтому просто число продаж
pipeline = [
    match_date_stage,
    {
        "$match": {
            "products.product_id": product_id,

        }
    }
]

result = db.supply_orders.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)
