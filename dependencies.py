from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


async def common_blah():
    return "world"


async def common_parameters(
        q: str | None = None,
        skip: int = 0,
        limit: int = 100,
        blah: str = Depends(common_blah)
):
    return {"q": q, "skip": skip, "limit": limit, "blah": blah}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/elements/")
async def read_elements(commons: CommonsDep):
    return commons
