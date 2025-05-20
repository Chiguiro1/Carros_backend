from fastapi import FastAPI
from routes.carros import router as carros_router

app = FastAPI()

app.include_router(carros_router)

