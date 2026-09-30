from fastapi import FastAPI
from app.routes.student_routes import router


app = FastAPI(
    title="Nishtha -003 CRUD API",
    description="FastAPI CRUD application",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Nishtha -003  CRUD API"
    }