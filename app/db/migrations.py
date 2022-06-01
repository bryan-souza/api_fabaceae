# Built-ins
import os

# Internals
from app.db import models
from app.db.database import engine
from app.dependencies import PathRouter

path_router = PathRouter()

def make_migrations():
    # Delete cache, just in case it's not a fresh install
    for file in path_router['CACHE_PATH'].iterdir():
        os.remove(file)

    # Create tables
    models.Base.metadata.create_all(bind=engine)
    
