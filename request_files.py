from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/file")
async def create_file(file: bytes = File(None, description="A file read as bytes")):
    if not file:
        return {"message": "No upload file sent"}
    return {"file": len(file)}


@app.post("/files")
async def create_file(
        files: Annotated[list[bytes], File(..., description="Multiple files as bytes")]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    return {"filename": file.filename}


@app.post("/uploadfiles")
async def create_upload_file(
        files: list[UploadFile] = File(..., description="Multiple files as UploadFile")
):
    return {"filename": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """

    return HTMLResponse(content=content)
