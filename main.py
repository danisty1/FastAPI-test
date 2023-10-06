from typing import List
from fastapi import FastAPI
from models import Article, Category, User
from fake_db import fake_articles,fake_categories,fake_users
# from database import users_data_from_db, categories_data_from_db, articles_data_from_db

app = FastAPI()

#получение всех пользователей, метод GET
@app.get("/users")
def get_users():
    return [user for user in fake_users]

#получение выбранного пользователя, метод GET
@app.get("/users/{user_id}")
def get_users(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

#получение всех категорий, метод GET
@app.get("/categories")
def get_categories():
    return [category for category in fake_categories]

#получение статьи в выбранной категории, метод GET
@app.get("/categories/{categoryName}/{title}")
def get_categories(categoryName, title):
    return [article for article in fake_articles if article.get("categoryName") == categoryName and article.get("title") == title]

#эндпоинт для новой категории, метод POST
@app.post("/addCategory")
def add_category(category: List[Category]):
    fake_categories.extend(category)
    return {"status": 200, "data": fake_categories}

#эндпоинт для добавления новой статьи, метод POST
@app.post("/addArticle")
def add_article(article: List[Article]):
    fake_articles.extend(article)
    return {"status": 200, "data": fake_articles}

#эндпоинт для добавления нового пользователя, метод POST
@app.post("/addUser")
def add_user(user: List[User]):
    fake_users.extend(user)
    return {"status": 200, "data": fake_users}