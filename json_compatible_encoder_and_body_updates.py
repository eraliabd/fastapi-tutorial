from datetime import datetime

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

#### json compatible encoder  ####
# fake_db = {}
#
#
# class Item(BaseModel):
#     title: str
#     timestamp: datetime
#     description: str | None = None
#
#
# @app.put("/items/{id}")
# async def update_item(id: str, item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatible_item_data
#     print(fake_db)
#     return "Success"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@app.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: str, item: Item):
    stored_item_data = items.get(item_id)
    print("stored_item_data: ", stored_item_data)

    if stored_item_data is not None:
        stored_item_model = Item(**stored_item_data)
    else:
        stored_item_model = Item()

    print("stored_item_model: ", stored_item_model)

    update_data = item.dict(exclude_unset=True)
    print("update_data: ", update_data)

    updated_item = stored_item_model.copy(update=update_data)
    print("update_item: ", updated_item)

    items[item_id] = jsonable_encoder(updated_item)
    print(items[item_id])

    return updated_item
