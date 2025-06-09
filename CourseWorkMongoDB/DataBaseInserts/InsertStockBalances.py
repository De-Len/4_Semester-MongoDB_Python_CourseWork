import datetime

from dateutil import parser
from pymongo import MongoClient
from bson.objectid import ObjectId

# 3
client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

quantities = [420, 107, 809, 203, 506, 780, 340, 901, 101, 607, 408, 250, 603, 380]

products_info = {
    "Универмаг на Ленина": [
        ("Футболка 'I Am Groot'", "665f1100a1a1a1a1a1a1a201"),
        ("Куртка Neo", "665f1100a1a1a1a1a1a1a201"),
    ],
    "Магазин на Весенней": [
        ("Лампа Пиксар", "665f1100a1a1a1a1a1a1a202"),
        ("Чайник SkyNet", "665f1100a1a1a1a1a1a1a202"),
    ],
    "Киоск на Терешковой": [
        ("ЛембиКолада", "665f1100a1a1a1a1a1a1a203"),
        ("Закуска 'Пресциоус'", "665f1100a1a1a1a1a1a1a203"),
    ],
    "Лоток на Гагарина": [
        ("Бэт-расческа", "665f1100a1a1a1a1a1a1a205"),
        ("Зеркало Волдеморта", "665f1100a1a1a1a1a1a1a205"),
    ],
    "Магазин на Рекордной": [
        ("Стол Дома Старка", "665f1100a1a1a1a1a1a1a204"),
        ("Табурет 'Мститель'", "665f1100a1a1a1a1a1a1a204"),
    ],
    "Киоск на Октябрьском": [
        ("Жвачка из Космоса", "665f1100a1a1a1a1a1a1a207"),
        ("Снэк Вуки", "665f1100a1a1a1a1a1a1a207"),
    ],
    "Универмаг на Соборной": [
        ("Чайник 'Гарри'", "665f1100a1a1a1a1a1a1a206"),
        ("Наушники 'Левиосаа'", "665f1100a1a1a1a1a1a1a206"),
    ],
}

def resolve_ids(products_info):
    result = {}

    for store_name, product_list in products_info.items():
        store = db.stores.find_one({"name": store_name}, {"_id": 1})
        if not store:
            print(f"[!] Магазин не найден: {store_name}")
            continue

        store_id = store["_id"]
        products_with_ids = []

        for product_name, supplier_id_str in product_list:
            supplier_id = ObjectId(supplier_id_str)
            product = db.products.find_one({
                "name": product_name,
                "supplier_id": supplier_id
            }, {"_id": 1})

            if not product:
                print(f"[!] Продукт не найден: {product_name} (поставщик {supplier_id_str})")
                continue

            products_with_ids.append({
                "product_id": product["_id"],
                "supplier_id": supplier_id,
                "name": product_name
            })

        result[store_name] = {
            "store_id": store_id,
            "products": products_with_ids
        }

    return result

# Пример вызова:
resolved = resolve_ids(products_info)
resolved_items = list(resolved.items())

for resolved_items_index in range(7):
    store, product = resolved_items[resolved_items_index]
    print(f"{store}: store_id={product['store_id']}")
    p1 = product["products"][0]
    p2 = product["products"][1]
    print(f"  - {p1['name']}: {p1['product_id']}")
    print(f"  - {p2['name']}: {p2['product_id']}")
    db.get_collection("stock_balances").insert_one(
        {
            "store_id": product['store_id'],
    "products": [
        {
            "product_id": p1['product_id'],
            "quantity": quantities[resolved_items_index]
        },
        {
            "product_id": p2['product_id'],
            "quantity": quantities[resolved_items_index + 1]
        }
    ]})
