from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_date: datetime | None = Body(None),
        end_date: datetime | None = Body(None),
        repeat_at: time | None = Body(None),
        process_after: timedelta | None = Body(None)
):
    start_process = start_date + process_after
    duration = end_date - start_date

    return {
        "item_id": item_id,
        "start_date": start_date,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }
