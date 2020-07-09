from fastapi import FastAPI

from .views import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(
    user.router,
    prefix='/users',
    tags=['users'],
    responses={404: {"description": "Not found"}}
)
