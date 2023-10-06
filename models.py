from pydantic import BaseModel, Field

#модель данных для новой категории
class Category(BaseModel):
    id: int
    categoryName: str

#модель данных для новой статьи
class Article(BaseModel):
    id: int
    category_name: str
    title: str
    content: str
    createdAt: str
    editedAt: str

#модель данных для нового пользователя
class User(BaseModel):
    id: int
    email: str
    password: str = Field(min_length=6) # делаю валидацию пароля, пароль должен быть >= 6
    role: str