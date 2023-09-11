from pydantic import BaseModel
from typing import Union, List


class User(BaseModel):
    username: str
    email: str
    password: str


class Supplier(BaseModel):
    name: str
    phone: str
    specialty: str


class Supply(BaseModel):
    name: str
    amount: Union[str, int, float]
    observations: str = None


class Receipt(BaseModel):
    products: List[str]
    supplier_id: str
    timestamp: str
