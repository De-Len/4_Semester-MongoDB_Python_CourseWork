from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

# номер заказа - его id
pipeline = [
    {
        "$match": {
            "customer": {"$exists": True}  # Только документы, где есть customer
        }
    },
    {
        "$group": {
            "_id": {
                "name": "$customer.name",
                "surname": "$customer.surname"
            },
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}  # Сортировка по убыванию количества
    }
]

result = db.sales.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(f"{doc['_id']['name']} {doc['_id']['surname']}: {doc['count']}")