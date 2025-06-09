from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta
import random

# 4
client = MongoClient()
db = client["CourseWork"]

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

employees_info = {
    "Универмаг на Ленина": [
        ObjectId("665f101aa1a1a1a1a1a1a101"),
        ObjectId("665f101aa1a1a1a1a1a1a102"),
        ObjectId("665f101aa1a1a1a1a1a1a103"),
    ],
    "Магазин на Весенней": [
        ObjectId("665f101aa1a1a1a1a1a1a104"),
        ObjectId("665f101aa1a1a1a1a1a1a105"),
    ],
    "Киоск на Терешковой": [
        ObjectId("665f101aa1a1a1a1a1a1a107"),
    ],
    "Лоток на Гагарина": [
        ObjectId("665f101aa1a1a1a1a1a1a108"),
    ],
    "Магазин на Рекордной": [
        ObjectId("665f101aa1a1a1a1a1a1a109"),
        ObjectId("665f101aa1a1a1a1a1a1a10a"),
    ],
    "Киоск на Октябрьском": [
        ObjectId("665f101aa1a1a1a1a1a1a10b"),
    ],
    "Универмаг на Соборной": [
        ObjectId("665f101aa1a1a1a1a1a1a10c"),
        ObjectId("665f101aa1a1a1a1a1a1a10d"),
    ],
}

# Получаем id-шники магазинов и продуктов
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
                "name": product_name
            })
        result[store_name] = {
            "store_id": store_id,
            "products": products_with_ids
        }
    return result

resolved = resolve_ids(products_info)

# Генерация случайной даты в 2025 году до 31 мая
def random_date_2025():
    start = datetime(2025, 1, 1)
    end = datetime(2025, 5, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

# Генерация 10 продаж
sales = []
for _ in range(10):
    store_name = random.choice(list(resolved.keys()))
    store_entry = resolved[store_name]
    store_id = store_entry["store_id"]
    product_entry = random.choice(store_entry["products"])
    product_id = product_entry["product_id"]

    # Получаем сотрудников только из словаря employees_info
    employees_in_store = employees_info.get(store_name)
    if not employees_in_store:
        print(f"[!] Нет сотрудников в магазине {store_name}, пропускаем продажу")
        continue

    employee_id = random.choice(employees_in_store)

    sale = {
        "store_id": store_id,
        "employee_id": employee_id,
        "product_id": product_id,
        "quantity": random.randint(1, 5),
        "date": random_date_2025(),
    }

    if any(x in store_name.lower() for x in ["универмаг", "магазин"]):
        sale["customer"] = {
            "name": random.choice(["Илья", "Мария", "Анна", "Дмитрий"]),
            "surname": random.choice(["Смирнов(а)", "Иванов(а)", "Кузнецов(а)", "Попов(а)"]),
            "reputation": random.randint(1, 10)
        }

    sales.append(sale)

# Вставка в коллекцию sales
db.sales.insert_many(sales)
print(f"[+] Вставлено {len(sales)} продаж.")