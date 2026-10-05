from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: int
    name: str
    description: Optional[str]
    price: float
    quantity: int
    category: str
