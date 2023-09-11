from pydantic import BaseModel
from typing import Union, List


class Users(BaseModel):
    username: str
    email: str
    password: str


class Suppliers(BaseModel):
    name: str
    phone: str
    specialty: str


class Supplies(BaseModel):
    name: str
    amount: Union[str, int, float]
    observations: str = None


class Receipts(BaseModel):
    products: List[str]
    supplier_id: str
    timestamp: str
