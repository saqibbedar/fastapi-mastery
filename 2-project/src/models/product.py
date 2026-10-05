# pydantic is validator for the data used to define the specs or interfaces
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    # here no need to define constructor as pydantic takes care of it. For ref, look at 1-project, we defined constructor and then invoked that in main.py. However, now we don't need it.
