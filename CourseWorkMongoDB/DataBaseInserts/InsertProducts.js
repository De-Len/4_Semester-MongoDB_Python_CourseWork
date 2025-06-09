// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("CourseWork");

db.getCollection("products").insertMany([
    // Универмаг на Ленина
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a301"),
        name: "Футболка 'I Am Groot'",
        description: "Футболка с принтом из Стражей Галактики",
        category: "Одежда",
        unit: "шт",
        price: 1200,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a201"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a302"),
        name: "Куртка Neo",
        description: "Чёрная кожаная куртка, вдохновлённая Матрицей",
        category: "Одежда",
        unit: "шт",
        price: 3200,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a201"),
    },

    // Магазин на Весенней
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a303"),
        name: "Лампа Пиксар",
        description: "Мини-лампа, вдохновлённая анимацией Pixar",
        category: "Товары для дома",
        unit: "шт",
        price: 1400,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a202"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a304"),
        name: "Чайник SkyNet",
        description: "Умный чайник с голосовым управлением (опасен)",
        category: "Бытовая техника",
        unit: "шт",
        price: 2500,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a202"),
    },

    // Киоск на Терешковой
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a305"),
        name: "ЛембиКолада",
        description: "Газировка со вкусом лембаса. Вдохновлено эльфами",
        category: "Продукты",
        unit: "бутылка",
        price: 70,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a203"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a306"),
        name: "Закуска 'Пресциоус'",
        description: "Шоколадка из Средиземья. Хочется сильно.",
        category: "Продукты",
        unit: "шт",
        price: 90,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a203"),
    },

    // Лоток на Гагарина
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a307"),
        name: "Бэт-расческа",
        description: "Гаджет Брюса Уэйна для волос",
        category: "Галантерея",
        unit: "шт",
        price: 120,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a205"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a308"),
        name: "Зеркало Волдеморта",
        description: "Смотришь — и тебя не существует",
        category: "Галантерея",
        unit: "шт",
        price: 180,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a205"),
    },

    // Магазин на Рекордной
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a309"),
        name: "Стол Дома Старка",
        description: "Мебель от Тони Старка — умный дизайн",
        category: "Мебель",
        unit: "шт",
        price: 2100,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a204"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a310"),
        name: "Табурет 'Мститель'",
        description: "Надежный, как Тор",
        category: "Мебель",
        unit: "шт",
        price: 1150,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a204"),
    },

    // Киоск на Октябрьском
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a311"),
        name: "Жвачка из Космоса",
        description: "Продукт с планеты Татуин",
        category: "Продукты",
        unit: "упаковка",
        price: 45,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a207"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a312"),
        name: "Снэк Вуки",
        description: "Любимая закуска Чубакки",
        category: "Продукты",
        unit: "упаковка",
        price: 65,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a207"),
    },

    // Универмаг на Соборной
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a313"),
        name: "Чайник 'Гарри'",
        description: "Кипятит воду как магия. Сова в комплект не входит",
        category: "Электроника",
        unit: "шт",
        price: 3100,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a206"),
    },
    {
        _id: ObjectId("675f301aa1a1a1a1a1a1a314"),
        name: "Наушники 'Левиосаа'",
        description: "Волшебный звук. Не ломаются заклинаниями.",
        category: "Электроника",
        unit: "шт",
        price: 2600,
        supplier_id: ObjectId("665f1100a1a1a1a1a1a1a206"),
    },
]);
