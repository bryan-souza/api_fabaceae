# Built-ins
from pathlib import Path

# Internals
from app.dependencies import PathRouter, get_db
from app.cerebrum import Identifier
from app.db import crud
from app.db.schemas import AIResult

# 3rd party
from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

path_router = PathRouter()
identifier = Identifier()


router = APIRouter(
    prefix="/ai",
    tags=["ai"]
)


@router.post('', response_model=AIResult)
async def identify_image(
    filename: Path = Body(..., embed=True),
    db: Session = Depends(get_db)
):
    
    # Check cache
    result = crud.get_result(db, digest=filename.stem)
    if result is not None:
        return result

    # Check if file was uploaded
    filepath = Path( path_router['CACHE_PATH'], filename )
    if not filepath.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    # AI Stuff
    plant_name, accuracy = identifier.identify_plant( filepath )
    result = crud.create_result(db, AIResult(digest=filename.stem,
                                             plant=plant_name,
                                             accuracy=accuracy))
    
    return result
