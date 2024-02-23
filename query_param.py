from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_item(
        item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {
                "description": "Reference site about Lorem Ipsum, giving information on its origins, "
                               "as well as a random Lipsum generator."
            }
        )

    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {
                "description": "Reference site about Lorem Ipsum, giving information on its origins, "
                               "as well as a random Lipsum generator."
            }
        )

    return item
