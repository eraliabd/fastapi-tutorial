from fastapi import FastAPI, Cookie, Header
from typing import Annotated

app = FastAPI()


@app.get("/items")
async def read_items(
        cookie_id: Annotated[str | None, Cookie()] = None,
        accept_encoding: Annotated[str | None, Header()] = None,
        sec_ch_ua: Annotated[str | None, Header()] = None,
        user_agent: Annotated[str | None, Header()] = None,
        x_token: Annotated[list[str] | None, Header()] = None
):
    results = {
        "cookie_id": cookie_id,
        "Accept-Encoding": accept_encoding,
        "Sec-Ch-Ua": sec_ch_ua,
        "User-Agent": user_agent,
        "X-Token values": x_token
    }
    return results
