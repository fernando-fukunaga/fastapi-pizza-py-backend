from pydantic import BaseModel


class AddSuppliers(BaseModel):
    name: str
    phone: str
    specialty: str