from fastapi import FastAPI

app = FastAPI

@app.get("/")
async def home():
    return {"msg": "App is running!"}

@app.post("/suppliers")
async def add_suppliers(supplier_schema):
    pass