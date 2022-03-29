# Built-ins
from pathlib import Path

# Internals
from app.dependencies import PathRouter

# 3rd party
from fastapi import APIRouter, UploadFile, File

path_router = PathRouter()

router = APIRouter(
    prefix="/files",
    tags=["files"]
)


@router.post('')
async def upload_file( 
    file: UploadFile = File(...)
):
    filepath = Path( path_router['CACHE_PATH'], file.filename )
    content = await file.read()

    with open(filepath, 'wb') as new_file:
        new_file.write(content)

    return { "filename": file.filename }
