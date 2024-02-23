from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items_validation/{item_id}")
async def read_item(
        item_id: int = Path(..., title="The ID of the item to get", gt=10),
        q: str | None = Query(None, alias="item-query"),
        size: float = Query(..., gt=0, lt=7.75)
):
    results = {"item_id": item_id, "size": size}

    if q:
        results.update({"q": q})

    return results

# gt, ge, lt, le
