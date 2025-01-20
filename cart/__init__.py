from products import dao
from typing import List, Dict, Any


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        """Represents a product with basic attributes."""
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: Dict[str, Any]) -> "Product":
        """Static method to create a Product instance from a dictionary."""
        return Product(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),
            cost=data.get("cost"),
            qty=data.get("qty", 0)
        )


def list_products() -> List[Product]:
    """Fetches and returns all products."""
    products_data = dao.list_products()
    return [Product.load(product) for product in products_data]  # Use list comprehension


def get_product(product_id: int) -> Product:
    """Fetches and returns a single product by ID."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)


def add_product(product: Dict[str, Any]):
    """Adds a new product to the database."""
    required_keys = {"id", "name", "description", "cost", "qty"}
    if not required_keys.issubset(product.keys()):
        raise ValueError(f"Product data is missing one or more required keys: {required_keys}")
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product."""
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    if not dao.get_product(product_id):
        raise ValueError(f"Product with ID {product_id} does not exist.")
    dao.update_qty(product_id, qty)
