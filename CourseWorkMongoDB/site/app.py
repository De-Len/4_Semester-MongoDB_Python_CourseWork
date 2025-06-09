from copy import deepcopy
from datetime import datetime

import bson
from flask import Flask, render_template, request, redirect, current_app, Blueprint, url_for, Response
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["CourseWork"]

app.config['MONGO_DB'] = db  # <- добавляем сюда базу

collection = db["items"]

@app.route("/")
def index():
    items = list(collection.find())
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    if name:
        collection.insert_one({"name": name})
    return redirect("/")

@app.route("/delete/<item_id>")
def delete(item_id):
    collection.delete_one({"_id": ObjectId(item_id)})
    return redirect("/")

@app.route("/update/<item_id>", methods=["POST"])
def update(item_id):
    new_name = request.form.get("new_name")
    if new_name:
        collection.update_one({"_id": ObjectId(item_id)}, {"$set": {"name": new_name}})
    return redirect("/")


employees_bp = Blueprint("employees", __name__, url_prefix="/add/employees")
@employees_bp.route("/", methods=["GET", "POST"])
def add_employee():
    db = current_app.config['MONGO_DB']
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        salary = int(request.form["salary"])
        db.employees.insert_one({
            "name": name,
            "surname": surname,
            "salary": salary
        })
        return redirect(url_for("employees.add_employee_success"))
    return render_template("add_employee.html")

@employees_bp.route("/success")
def add_employee_success():
    return render_template("add_employee_success.html")
app.register_blueprint(employees_bp)


products_bp = Blueprint("products", __name__, url_prefix="/add/products")
@products_bp.route("/", methods=["GET", "POST"])
def add_product():
    db = current_app.config['MONGO_DB']
    if request.method == "POST":
        name = request.form["name"]
        description = request.form.get("description", "")
        category = request.form.get("category", "")
        unit = request.form.get("unit", "")
        price = float(request.form.get("price", 0))
        supplier_id_str = request.form.get("supplier_id")

        # Если передали supplier_id, преобразуем в ObjectId, иначе None
        supplier_id = ObjectId(supplier_id_str) if supplier_id_str else None

        product_doc = {
            "name": name,
            "description": description,
            "category": category,
            "unit": unit,
            "price": price,
        }
        if supplier_id:
            product_doc["supplier_id"] = supplier_id

        db.products.insert_one(product_doc)
        return redirect(url_for("products.add_product_success"))

    # Для GET можно отдать форму (в шаблоне можно предусмотреть)
    return render_template("add_product.html")

@products_bp.route("/success")
def add_product_success():
    return render_template("add_product_success.html")
app.register_blueprint(products_bp)


sales_bp = Blueprint("sales", __name__, url_prefix="/add/sales")
@sales_bp.route("/", methods=["GET", "POST"])
def add_sale():
    if request.method == "POST":
        store_id = request.form["store_id"]
        employee_id = request.form["employee_id"]
        product_id = request.form["product_id"]
        quantity = int(request.form["quantity"])
        date_str = request.form["date"]

        # Преобразуем дату из строки в datetime
        date = datetime.strptime(date_str, "%Y-%m-%d")

        sale_doc = {
            "store_id": ObjectId(store_id),
            "employee_id": ObjectId(employee_id),
            "product_id": ObjectId(product_id),
            "quantity": quantity,
            "date": date
        }

        db.sales.insert_one(sale_doc)
        return redirect(url_for("sales.add_sale_success"))

    # Для GET — подгружаем магазины, сотрудников и продукты
    stores = list(db.stores.find())
    employees = list(db.employees.find())
    products = list(db.products.find())

    return render_template("add_sale.html", stores=stores, employees=employees, products=products)

@sales_bp.route("/success")
def add_sale_success():
    return render_template("add_sale_success.html")
app.register_blueprint(sales_bp)


def convert_objectid(doc):
    if isinstance(doc, dict):
        for k, v in doc.items():
            if isinstance(v, ObjectId):
                doc[k] = str(v)
            elif isinstance(v, list):
                doc[k] = [convert_objectid(i) if isinstance(i, dict) else i for i in v]
            elif isinstance(v, dict):
                doc[k] = convert_objectid(v)
    return doc

stock_balances_bp = Blueprint("stock_balances", __name__, url_prefix="/add/stock_balances")
@stock_balances_bp.route("/", methods=["GET", "POST"])
def add_stock_balance():
    if request.method == "POST":
        store_id = request.form["store_id"]
        product_ids = request.form.getlist("product_id")
        quantities = request.form.getlist("quantity")

        products_list = []
        for pid, qty in zip(product_ids, quantities):
            if pid and qty:
                products_list.append({
                    "product_id": ObjectId(pid),
                    "quantity": int(qty)
                })

        stock_balance_doc = {
            "store_id": ObjectId(store_id),
            "products": products_list
        }

        db.stock_balances.insert_one(stock_balance_doc)
        return redirect(url_for("stock_balances.add_stock_balance_success"))

    stores = [convert_objectid(s) for s in list(db.stores.find())]
    products = [convert_objectid(p) for p in list(db.products.find())]

    for store in stores:
        store["_id"] = str(store["_id"])
    for product in products:
        product["_id"] = str(product["_id"])

    return render_template("add_stock_balance.html", stores=stores, products=products)

@stock_balances_bp.route("/success")
def add_stock_balance_success():
    return render_template("add_stock_balance_success.html")
app.register_blueprint(stock_balances_bp)


stores_bp = Blueprint("stores", __name__, url_prefix="/add/stores")
@stores_bp.route("/", methods=["GET", "POST"])
def add_store():
    if request.method == "POST":
        # Получаем данные из формы
        type_ = request.form.get("type")
        name = request.form.get("name")
        section_names = request.form.get("section_names", "")
        hall_names = request.form.get("hall_names", "")
        cash_registers_number = request.form.get("cash_registers_number", 0)
        area = request.form.get("area", 0)

        # Преобразуем поля, где нужно
        section_names_list = [s.strip() for s in section_names.split(",")] if section_names else []
        hall_names_list = [h.strip() for h in hall_names.split(",")] if hall_names else []

        try:
            cash_registers_number = int(cash_registers_number)
        except ValueError:
            cash_registers_number = 0

        try:
            area = int(area)
        except ValueError:
            area = 0

        store_doc = {
            "type": type_,
            "name": name,
            "section_names": section_names_list,
            "hall_names": hall_names_list,
            "cash_registers_number": cash_registers_number,
            "area": area,
            "payments": []
        }

        db.stores.insert_one(store_doc)
        return redirect(url_for("stores.add_store_success"))

    return render_template("add_store.html")

@stores_bp.route("/success")
def add_store_success():
    return render_template("add_store_success.html")
app.register_blueprint(stores_bp)

suppliers_bp = Blueprint("suppliers", __name__, url_prefix="/add/suppliers")
@suppliers_bp.route("/", methods=["GET", "POST"])
def add_supplier():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            supplier_doc = {
                "name": name
            }
            db.suppliers.insert_one(supplier_doc)
            return redirect(url_for("suppliers.add_supplier_success"))
    return render_template("add_supplier.html")

@suppliers_bp.route("/success")
def add_supplier_success():
    return render_template("add_supplier_success.html")
app.register_blueprint(suppliers_bp)


supply_orders_bp = Blueprint("supply_orders", __name__, url_prefix="/add/supply_orders")
@supply_orders_bp.route("/", methods=["GET", "POST"])
def add_supply_order():
    if request.method == "POST":
        store_id = request.form["store_id"]
        date_str = request.form["date"]

        # Преобразуем дату
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # Продукты: список из product_id и quantity
        # Ожидаем, что формы содержат product_id[] и quantity[]
        product_ids = request.form.getlist("product_id")
        quantities = request.form.getlist("quantity")

        products = []
        for pid, qty in zip(product_ids, quantities):
            if pid and qty:
                products.append({
                    "product_id": ObjectId(pid),
                    "quantity": int(qty)
                })

        supply_order_doc = {
            "store_id": ObjectId(store_id),
            "date": date,
            "products": products
        }

        db.supply_orders.insert_one(supply_order_doc)
        return redirect(url_for("supply_orders.add_supply_order_success"))

    stores = list(db.stores.find())
    products = list(db.products.find())
    return render_template("add_supply_order.html", stores=stores, products=products)

@supply_orders_bp.route("/success")
def add_supply_order_success():
    return render_template("add_supply_order_success.html")
app.register_blueprint(supply_orders_bp)


supply_requests_bp = Blueprint("supply_requests", __name__, url_prefix="/add/supply_requests")
@supply_requests_bp.route("/", methods=["GET", "POST"])
def add_supply_request():
    if request.method == "POST":
        store_id = request.form["store_id"]
        date_str = request.form["date"]

        date = datetime.strptime(date_str, "%Y-%m-%d")

        product_ids = request.form.getlist("product_id")
        quantities = request.form.getlist("quantity")

        products = []
        for pid, qty in zip(product_ids, quantities):
            if pid and qty:
                products.append({
                    "product_id": ObjectId(pid),
                    "quantity": int(qty)
                })

        supply_request_doc = {
            "store_id": ObjectId(store_id),
            "date": date,
            "products": products
        }

        db.supply_requests.insert_one(supply_request_doc)
        return redirect(url_for("supply_requests.add_supply_request_success"))

    stores = list(db.stores.find())
    products = list(db.products.find())
    return render_template("add_supply_request.html", stores=stores, products=products)

@supply_requests_bp.route("/success")
def add_supply_request_success():
    return render_template("add_supply_request_success.html")
app.register_blueprint(supply_requests_bp)


COLLECTIONS = [
    {"name": "Сотрудники", "key": "employees"},
    {"name": "Продукты", "key": "products"},
    {"name": "Продажи", "key": "sales"},
    {"name": "Остатки", "key": "stock_balances"},
    {"name": "Магазины", "key": "stores"},
    {"name": "Поставщики", "key": "suppliers"},
    {"name": "Поставки", "key": "supply_orders"},
    {"name": "Заявки", "key": "supply_requests"},
]


@app.route('/view/<collection>')
def view_collection(collection):
    if collection not in [c["key"] for c in COLLECTIONS]:
        return "Коллекция не найдена", 404
    docs = list(db[collection].find())
    # Передаем COLLECTIONS для использования отображаемых имен
    return render_template('view_collection.html', collection=collection, collections=COLLECTIONS, docs=docs)

@app.route('/delete/<collection>/<doc_id>', methods=['POST'])
def delete_doc(collection, doc_id):
    if collection not in [c["key"] for c in COLLECTIONS]:
        return "Коллекция не найдена", 404
    db[collection].delete_one({"_id": ObjectId(doc_id)})
    return redirect(url_for('view_collection', collection=collection))

@app.route('/view/all_collections')
def view_all_collections():
    all_docs = []
    for coll in COLLECTIONS:
        docs = list(db[coll["key"]].find())
        all_docs.append({
            "name": coll["name"],
            "key": coll["key"],
            "docs": docs
        })
    return render_template('view_all_collections.html', collections=all_docs)


@app.route("/edit/<collection>/<doc_id>", methods=["GET", "POST"])
def edit_doc(collection, doc_id):
    if collection not in [c["key"] for c in COLLECTIONS]:
        return "Коллекция не найдена", 404
    coll = db[collection]
    doc = coll.find_one({"_id": ObjectId(doc_id)})
    if not doc:
        return "Документ не найден", 404

    # Копируем, чтобы не менять исходный документ
    editable_doc = deepcopy(doc)
    editable_doc["_id"] = str(editable_doc["_id"])

    if request.method == "POST":
        update_data = {}
        for key, value in request.form.items():
            if key == "_id":
                continue
            # Преобразуем по простым правилам, расширяйте вручную при необходимости
            if value.isdigit():
                value = int(value)
            elif value.replace('.', '', 1).isdigit() and '.' in value:
                value = float(value)
            elif value.lower() == 'none':
                value = None
            update_data[key] = value

        coll.update_one({"_id": ObjectId(doc_id)}, {"$set": update_data})
        return redirect(url_for('view_collection', collection=collection))

    return render_template("edit_doc.html", collection=collection, doc=editable_doc)

if __name__ == "__main__":
    app.run(debug=True)





