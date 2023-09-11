from database_config import database
import src.models as models
from typing import List

supplier_collection = database["suppliers"]


def add_suppliers(supplier: models.Supplier) -> models.Supplier:
    document = {
        "name":supplier.name,
        "phone":supplier.phone,
        "specialty":supplier.specialty
    }
    supplier_collection.insert_one(document)
    return supplier


def list_suppliers() -> List[models.Supplier]:
    supplier_list = []
    
    for supplier in supplier_collection.find():
        supplier_list.append(supplier)

    return supplier_list
