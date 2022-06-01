from sqlalchemy.orm import Session

from app.db import models, schemas

# Create
def create_result(db: Session, result: schemas.AIResult):
    db_result = models.AIResult(digest=result.digest, 
                                plant=result.plant, 
                                accuracy=result.accuracy)

    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

# Read
def get_result(db: Session, digest: str):
    return db.query(models.AIResult).filter(models.AIResult.digest == digest).first()