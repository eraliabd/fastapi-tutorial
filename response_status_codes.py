from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


@app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(pk: str):
    print("pk", pk)
    return {"pk": pk}


@app.get("/items", status_code=status.HTTP_302_FOUND)
async def read_item_redirect():
    return {"hello": "world"}

