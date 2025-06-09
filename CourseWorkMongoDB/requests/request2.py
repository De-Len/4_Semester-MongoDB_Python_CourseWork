from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]


start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 5, 31, 23, 59, 59)

match_stage = {
    "$match": {
        "date": {
            "$gte": start_date,
            "$lte": end_date
        }
    }
}

# попались без фиксированных покупателей, поэтому просто число продаж
pipeline = [
    {
        "$match": {
            "quantity": { "$gt": 1}
        }
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "_id",
            "as": "product",
        }
    },
    match_stage,
    {
        "$match": {
            "product.category": "Продукты"
        }
    }
]

result = db.sales.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)

print("Число продаж: " + str(len(result_list)))
