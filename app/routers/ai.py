# Built-ins
from pathlib import Path

# Internals
from app.dependencies import PathRouter
from app.cerebrum import Identifier

# 3rd party
from fastapi import APIRouter, Body
from fastapi.exceptions import HTTPException

path_router = PathRouter()
identifier = Identifier()


router = APIRouter(
    prefix="/ai",
    tags=["ai"]
)


@router.post('')
async def identify_image(
    filename: str = Body(..., embed=True)
):
    try:
        filepath = Path(
            path_router['CACHE_PATH'], 
            filename
        )
    except:
        raise HTTPException(
            status_code=400,
            detail="File not found"
        )

    if not ( filepath.is_file() ):
        raise HTTPException(
            status_code=400,
            detail="Not a file"
        )

    plant_name, accuracy = identifier.identify_plant( filepath )
    return {
        "plant": plant_name,
        "accuracy": accuracy
    }

