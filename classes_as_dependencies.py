from fastapi import FastAPI, Depends
from typing import Annotated, Any

app = FastAPI()


class Cat:
    def __init__(self, name: str):
        self.name = name


fluffy = Cat("Mr Fluffy")


fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
# async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
# async def read_items(commons: CommonQueryParams = Depends()):
# async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
async def read_items(commons: Annotated[Any, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})

    items = fake_item_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
