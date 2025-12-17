from fastapi import FastAPI
from app.routers import product_router

app = FastAPI(title="Inventory API", version="1.0.0")

app.include_router(product_router.router)

@app.get("/")
async def root():
    return {"message": "Inventory System Online 🚀"}