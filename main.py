from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int
    name: str = Field(max_length=20)
    surname: str = Field(max_length=20)
    age: int = Field(ge=1)
    country: str = Field(max_length=20)

users = []

# Эндпоинт для получения всех пользователей
@app.get("/users")
def get_users():
    return users

# Эндпоинт для получения пользователя по ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user
    return {"error": "Пользователь не найден"}

# Эндпоинт для создания нового пользователя
@app.post("/users")
def create_user(user: User):
    users.append(user.dict())
    return user

# Эндпоинт для обновления пользователя
@app.patch("/users/{user_id}")
def update_user(user_id: int, user: User):
    for index, u in enumerate(users):
        if u['id'] == user_id:
            users[index] = user.dict()
            return {"message": "Пользователь обновлен"}
    return {"error": "Пользователь не найден"}

# Эндпоинт для удаления пользователя
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            del users[index]
            return {"message": "Пользователь удален"}
    return {"error": "Пользователь не найден"}
