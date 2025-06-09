from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]


start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 5, 31, 23, 59, 59)

match_stage = {
    "$match": {
        "date": {
            "$gte": start_date,
            "$lte": end_date
        },
        "products.quantity": { "$gt": 30 }
    }
}

pipeline = [
    {
        "$unwind": "$products"
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "products.product_id",
            "foreignField": "_id",
            "as": "product",
        }
    },
    match_stage,
    {
        "$lookup": {
            "from": "suppliers",
            "localField": "product.supplier_id",
            "foreignField": "_id",
            "as": "supplier",
        }
    },
    {
        "$group": {
            "_id": None,
            "unique_suppliers": { "$addToSet": "$supplier" }
        }
    },
    {
        "$project": {
            "_id": 0
        }
    }

]

result = db.supply_orders.aggregate(pipeline)
for doc in result:
    print(doc)