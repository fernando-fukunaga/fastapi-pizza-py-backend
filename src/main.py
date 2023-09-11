from fastapi import FastAPI
import src.schemas as schemas
'''import src.suppliers_repository as suppliers_repository
import src.models as models'''
from src.database_config import database    

app = FastAPI()

@app.get("/")
async def home():
    return {"msg": "App is running!"}

@app.post("/suppliers")
async def add_suppliers(supplier: schemas.AddSuppliers):
    document = {
        "name":supplier.name,
        "phone":supplier.phone,
        "specialty":supplier.specialty
    }
    database["clients"].insert_one(document)
    return supplier
