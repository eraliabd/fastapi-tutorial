from fastapi import FastAPI, Form, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    print("password:", password)
    return {"username": username}


@app.post("/login-json")
async def login_json(username: str = Body(...), password: str = Body(...)):
    print("password:", password)
    return {"username": username}
