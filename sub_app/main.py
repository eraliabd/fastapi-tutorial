from fastapi import FastAPI, Depends, HTTPException

from sub_app.dependencies import get_query_token
# todo: import routers
from sub_app.routers import users_router, items_router

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users_router)
app.include_router(items_router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications"}
