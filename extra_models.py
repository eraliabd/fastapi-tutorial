from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Literal, Union

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("user_in.dict", user_in.dict())
    print("User `saved`.")
    return user_in_db


@app.post("/user", response_model=UserOut)
async def read_item(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5
    }
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]


class ListItem(BaseModel):
    name: str
    description: str


list_items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/list_items", response_model=list[ListItem])
async def read_items():
    return list_items


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.4, "bar": 5.6}
