from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]


employee_id = db.employees.find_one({
    "name": "Людмила",
    "surname": "Синицина",
})["_id"]
print(employee_id)

store_id = db.stores.find_one({"name": "Универмаг на Соборной"}) ["_id"]
print(store_id)

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 5, 31, 23, 59, 59)

match_stage = {
    "$match": {
        "date": {
            "$gte": start_date,
            "$lte": end_date
        },
        "store_id": store_id,
        "employee_id": employee_id
    }
}

pipeline = [
    match_stage,
]

result = db.sales.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print(doc)


