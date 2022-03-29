# Internals
from app.routers import files, ai

# 3rd party
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Middlewares

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Routes

app.include_router(ai.router)
app.include_router(files.router)
