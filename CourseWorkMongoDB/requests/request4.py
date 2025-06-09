from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

# обязательно указывать какого поставщика
product_id = db.products.find_one({
    "name": "Футболка 'I Am Groot'",
    "supplier_id": ObjectId("665f1100a1a1a1a1a1a1a201")
})["_id"]
# print(product_id)

product_price = db.products.find_one({
    "name": "Футболка 'I Am Groot'",
    "supplier_id": ObjectId("665f1100a1a1a1a1a1a1a201")
})["price"]
# print(product_price)

# указанного типа
stores_cursor = db.stores.find({"type": "Универмаг"})
stores_id = [store["_id"] for store in stores_cursor]
# print(stores_id)


pipeline = [
    {
        "$match": {
            "products.product_id": product_id,
            "store_id": {"$in": stores_id}
        }
    },
    {
        "$project": {
            "products.quantity": 1
        }
    }

]

result = db.stock_balances.aggregate(pipeline)
result_list = list(result)

for doc in result_list:
    print("Количество: " + str(doc['products']))

print("Цена: " + str(product_price))

