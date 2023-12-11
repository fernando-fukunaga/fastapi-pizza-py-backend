from fastapi import FastAPI
import src.repositories.suppliers_repository as suppliers_repository
import src.models as models   

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "App is running!"}


@app.post("/suppliers")
async def add_suppliers(supplier: models.Supplier):
    return suppliers_repository.add_suppliers(supplier)


@app.get("/suppliers")
async def list_suppliers():
    return suppliers_repository.list_suppliers()
