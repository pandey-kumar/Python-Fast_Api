from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as reviews_router
# Lets add some the things in starting using lifespan

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("***lifespan started")
    create_tables()
    print("***Tables Created SuccessFully")
    yield

    # Lets do shutdown and cleanup here
    print("***app Is Getting shut down***")


app=FastAPI(
    title="RangManch Reviews API",
    description="Theatre review API for pune RangManch",
    lifespan=lifespan
)


app.include_router(reviews_router)

@app.get("/")
def root():
    return{"message":"Welcome to RangManch API"}