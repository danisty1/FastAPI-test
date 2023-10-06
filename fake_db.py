# фейковые данные, так как не успел разобраться, как распарсить в json формат кортеж кортежей, который приходит из БД 😢
fake_users = [
    {"id": 1, "email": "john@wick.com", "password": "qwerty123", "role": "admin"},
    {"id": 2, "email": "walter@white.com", "password": "123123", "role": "editor"},
    {"id": 3, "email": "baet@wert.com", "password": "qw3123", "role": "user"}
]

fake_categories = [
    {"id": 1, "categoryName": "Common"},
    {"id": 2, "categoryName": "Rare"}
]

fake_articles = [
    {"id": 1, "categoryName": "Common", "title": "Статья как вязать", "content": "В этой статье вы научитесь, как вязать крестиком", "created_at": "24-11-23", "edited_at": "25-11-23"},
    {"id": 2, "categoryName": "Common", "title": "Статья как програмиировать", "content": "В этой статье вы научитесь выводить Hello world в консоль", "created_at": "24-11-23", "edited_at": "25-11-23"},
    {"id": 3, "categoryName": "Common", "title": "Статья как шить", "content": "В этой статье вы научитесь шить", "created_at": "24-11-23", "edited_at": "25-11-23"}
]