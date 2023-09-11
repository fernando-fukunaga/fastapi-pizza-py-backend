from odmantic import Model
from typing import Union, List
from datetime import datetime


class Users(Model):
    username: str
    email: str
    password: str


class Suppliers(Model):
    name: str
    phone: str
    specialty: str


class Supplies(Model):
    name: str
    amount: Union[str, int, float]
    observations: str = None


class Receipts(Model):
    products: List[str]
    supplier_id: str
    timestamp: str
