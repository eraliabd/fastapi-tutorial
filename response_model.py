from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, EmailStr
from typing import Literal

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.4
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.3},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 63, "tax": 49.3},
    "baz": {"name": "Baz", "description": None, "price": 34.2, "tax": 45.4, "tags": []}
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item


class UserBase(BaseModel):
    username: str
    email: str  # EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"}
)
async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]


@app.get(
    "/items/{item_id}/public",
    response_model=Item,
    response_model_exclude={"tax"}
)
async def read_item_public_data(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]
