from fastapi import FastAPI, Depends, Header, HTTPException, status
from typing import Annotated

app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Token header invalid")
    return "hello"


async def verify_key(x_key: Annotated[str, Header(...)]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Key header invalid")
    return x_key


# GLOBAL DEPENDENCIES
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


# @app.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)], tags=["items"])
@app.get("/items")
async def read_items_token_key():
    return [{"item": "Foo"}, {"item": "Bar"}]


# @app.get("/users", dependencies=[Depends(verify_token), Depends(verify_key)], tags=["users"])
@app.get("/users")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
