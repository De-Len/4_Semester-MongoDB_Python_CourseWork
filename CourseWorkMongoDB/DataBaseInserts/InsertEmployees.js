// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("CourseWork");

db.getCollection("employees").insertMany([
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a101"),
        name: "Иван",
        surname: "Жмых",
        salary: 40000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a102"),
        name: "Василий",
        surname: "Петров",
        salary: 25000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a103"),
        name: "Роман",
        surname: "Бондарь",
        salary: 60000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a104"),
        name: "Питер",
        surname: "Паркер",
        salary: 20000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a105"),
        name: "Сергей",
        surname: "Смит",
        salary: 35000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a106"),
        name: "Георгий",
        surname: "Филимонов",
        salary: 50000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a107"),
        name: "Анна",
        surname: "Евтушенко",
        salary: 20000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a108"),
        name: "Марина",
        surname: "Гоголь",
        salary: 25000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a109"),
        name: "Олег",
        surname: "Козлов",
        salary: 27000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a10a"),
        name: "Андрей",
        surname: "Калинин",
        salary: 33000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a10b"),
        name: "Алексей",
        surname: "Миронов",
        salary: 45000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a10c"),
        name: "Людмила",
        surname: "Синицина",
        salary: 30000,
    },
    {
        _id: ObjectId("665f101aa1a1a1a1a1a1a10d"),
        name: "Татьяна",
        surname: "Ларина",
        salary: 27000,
    },
]);
