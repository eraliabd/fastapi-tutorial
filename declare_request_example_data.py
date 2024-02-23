from fastapi import FastAPI, Path, Query, Body, Form, File, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


class ItemModel(BaseModel):
    name: str = Field(..., examples=["Foo"])
    description: str | None = Field(None, examples=["A very nice Item"])
    price: float = Field(..., examples=[16.25])
    tax: float | None = Field(None, examples=[1.67])


@app.put("/items/{item_id}")
async def update_item_model(item_id: int, item: ItemModel):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/{item_id}")
async def update_item_model2(
        item_id: int,
        item: ItemModel = Body(
            ...,
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice item",
                    "price": 16.11,
                    "tax": 3.2
                },
                {
                    "name": "Bar",
                    "price": 45.23
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four"
                }
            ]
        )
):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/{item_id}")
async def update_item2(
        item_id: int,
        item: ItemModel = Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item"
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastApi can convert price `string` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": 35.4
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected  with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four"
                    }
                }
            }
        )
):
    results = {"item_id": item_id, "item": item}
    return results
