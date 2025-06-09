// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("CourseWork");

// Find a document in a collection.
db.getCollection("suppliers").insertMany([
    {
        _id: ObjectId("665f1100a1a1a1a1a1a1a201"),
        name: "Wakanda Textiles Inc.",
    }, // Чёрная пантера
    { _id: ObjectId("665f1100a1a1a1a1a1a1a202"), name: "Skynet Electronics" }, // Терминатор
    { _id: ObjectId("665f1100a1a1a1a1a1a1a203"), name: "Hobbiton Groceries" }, // Властелин колец
    {
        _id: ObjectId("665f1100a1a1a1a1a1a1a204"),
        name: "Stark Industries Furniture",
    }, // Железный человек
    { _id: ObjectId("665f1100a1a1a1a1a1a1a205"), name: "Gotham Accessories" }, // Бэтмен
    {
        _id: ObjectId("665f1100a1a1a1a1a1a1a206"),
        name: "Hogwarts Books & Scrolls",
    }, // Гарри Поттер
    { _id: ObjectId("665f1100a1a1a1a1a1a1a207"), name: "Galactic Trinkets" }, // Звёздные войны
]);
