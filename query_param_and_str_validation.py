from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get("/items")
async def read_items(q: str | None = Query(None, max_length=10, min_length=3, pattern="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@app.get("/items/1")
async def read_items(q: list[str] = Query(["abc", "cba"])):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@app.get("/items/2")
async def read_items(
        q: str | None = Query(None,
                              max_length=10,
                              min_length=3,
                              title="Sample query string",
                              description="This is a sample query string",
                              alias="item-query"
                              )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@app.get("/items/hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}

    return {"hidden_query": "Not found"}
