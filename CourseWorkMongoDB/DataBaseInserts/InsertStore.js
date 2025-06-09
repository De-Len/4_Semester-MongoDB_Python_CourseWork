// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("CourseWork");

// Find a document in a collection.
db.getCollection("stores").insertMany([
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a201"),
        type: "Универмаг",
        name: "Универмаг на Ленина",
        section_names: ["Одежда", "Обувь"],
        hall_names: ["Главный", "Детский"],
        cash_registers_number: 5,
        area: 210,
        payments: [
            {
                area_payment: 210000,
                utilities_payment: 15000,
                payment_date: ISODate("2025-03-01"),
            },
            {
                area_payment: 210000,
                utilities_payment: 15000,
                payment_date: ISODate("2025-04-01"),
            },
        ],
        employees: [
            ObjectId("665f101aa1a1a1a1a1a1a101"),
            ObjectId("665f101aa1a1a1a1a1a1a102"),
            ObjectId("665f101aa1a1a1a1a1a1a103"),
        ],
    },
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a202"),
        type: "Магазин",
        name: "Магазин на Весенней",
        hall_names: ["Зал 1", "Зал 2"],
        cash_registers_number: 3,
        area: 110,
        payments: [
            {
                area_payment: 110000,
                utilities_payment: 5000,
                payment_date: ISODate("2025-03-01"),
            },
            {
                area_payment: 110000,
                utilities_payment: 5000,
                payment_date: ISODate("2025-04-01"),
            },
            {
                area_payment: 110000,
                utilities_payment: 5000,
                payment_date: ISODate("2025-05-01"),
            },
        ],
        employees: [
            ObjectId("665f101aa1a1a1a1a1a1a104"),
            ObjectId("665f101aa1a1a1a1a1a1a105"),
        ],
    },
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a203"),
        type: "Киоск",
        name: "Киоск на Терешковой",
        cash_registers_number: 1,
        area: 5,
        payments: [
            {
                area_payment: 15000,
                utilities_payment: 200,
                payment_date: ISODate("2025-03-01"),
            },
            {
                area_payment: 15000,
                utilities_payment: 200,
                payment_date: ISODate("2025-04-01"),
            },
        ],
        employees: [ObjectId("665f101aa1a1a1a1a1a1a107")],
    },
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a204"),
        type: "Лоток",
        name: "Лоток на Гагарина",
        cash_registers_number: 1,
        area: 1,
        payments: [
            { area_payment: 1000, payment_date: ISODate("2025-04-01") },
            { area_payment: 1000, payment_date: ISODate("2025-05-01") },
            { area_payment: 1000, payment_date: ISODate("2025-06-01") },
        ],
        employees: [ObjectId("665f101aa1a1a1a1a1a1a108")],
    },
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a205"),
        type: "Магазин",
        name: "Магазин на Рекордной",
        hall_names: ["Основной зал"],
        cash_registers_number: 2,
        area: 100,
        payments: [
            {
                area_payment: 100000,
                utilities_payment: 5500,
                payment_date: ISODate("2025-03-01"),
            },
            {
                area_payment: 100000,
                utilities_payment: 5500,
                payment_date: ISODate("2025-04-01"),
            },
        ],
        employees: [
            ObjectId("665f101aa1a1a1a1a1a1a109"),
            ObjectId("665f101aa1a1a1a1a1a1a10a"),
        ],
    },
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a206"),
        type: "Киоск",
        name: "Киоск на Октябрьском",
        cash_registers_number: 1,
        area: 4,
        payments: [
            {
                area_payment: 14000,
                utilities_payment: 300,
                payment_date: ISODate("2025-03-01"),
            },
            {
                area_payment: 14000,
                utilities_payment: 300,
                payment_date: ISODate("2025-04-01"),
            },
            {
                area_payment: 14000,
                utilities_payment: 300,
                payment_date: ISODate("2025-06-01"),
            },
        ],
        employees: [ObjectId("665f101aa1a1a1a1a1a1a10b")],
    },
    {
        _id: ObjectId("665f201aa1a1a1a1a1a1a207"),
        type: "Универмаг",
        name: "Универмаг на Соборной",
        section_names: ["Электроника", "Техника"],
        hall_names: ["Этаж 1", "Этаж 2", "Цоколь"],
        cash_registers_number: 6,
        area: 240,
        payments: [
            {
                area_payment: 230000,
                utilities_payment: 16000,
                payment_date: ISODate("2025-03-01"),
            },
            {
                area_payment: 230000,
                utilities_payment: 16000,
                payment_date: ISODate("2025-04-01"),
            },
            {
                area_payment: 230000,
                utilities_payment: 16000,
                payment_date: ISODate("2025-05-01"),
            },
            {
                area_payment: 230000,
                utilities_payment: 16000,
                payment_date: ISODate("2025-06-01"),
            },
        ],
        employees: [
            ObjectId("665f101aa1a1a1a1a1a1a10c"),
            ObjectId("665f101aa1a1a1a1a1a1a10d"),
        ],
    },
]);
