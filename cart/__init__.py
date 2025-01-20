import json

from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    """Fetches the cart contents for a user."""
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Parse all product IDs from cart details and avoid redundant loops
    items = []
    for cart_detail in cart_details:
        contents = json.loads(cart_detail['contents'])
        items.extend(contents)  # Merge all contents into one list

    # Fetch products for all the items
    products_list = [products.get_product(i) for i in items]
    return products_list


def add_to_cart(username: str, product_id: int):
    """Adds a product to the user's cart."""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """Removes a product from the user's cart."""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """Deletes the entire cart for the user."""
    dao.delete_cart(username)
