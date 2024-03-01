from email._header_value_parser import get_value

from fastapi import FastAPI, Depends, Body, Cookie
from typing import Annotated

app = FastAPI()


async def needy_dependency(fresh_value: Annotated[str, Depends(get_value, use_cache=False)]):
    return {"fresh_value": fresh_value}


def query_extractor(q: str | None = None):
    return q


def query_or_body_extractor(
        q: Annotated[str, Depends(query_extractor)],
        last_query: str | None = Cookie(None)
):
    if q:
        return q
    return last_query


@app.post("/item")
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {"query_or_body": query_or_body}
