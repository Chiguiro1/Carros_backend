from fastapi import FastAPI
from routes.carros import router as carros_router

app = FastAPI()

app.include_router(carros_router)

@app.get("/")
def a():
    return {"message":"Hola, por favor ir a http://localhost:8020/docs para ver los endpoints Gracias"}


