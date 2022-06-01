from pydantic import BaseModel

class AIResult(BaseModel):
    digest: str
    plant: str
    accuracy: float

    class Config:
        orm_mode = True