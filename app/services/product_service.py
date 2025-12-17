from typing import List, Optional
from uuid import UUID, uuid4
from app.database import products_db
from app.models.product_model import Product

def get_all_products() -> List[Product]:
    return products_db

def get_product_by_uuid(product_id: UUID) -> Optional[Product]:
    for product in products_db:
        if product.id == product_id:
            return product
    return None

def create_product(product: Product)-> Product:
    products_db.append(product)
    return product

def update_product(product_id: UUID, new_product: Product) -> Product:
    for index, current_product in enumerate(products_db):
        if(current_product.id == product_id):
            updated_product = new_product.copy(update={
                "id": product_id,
                "created_at": current_product.created_at
            })

            products_db[index] = updated_product
            return updated_product
    return None

def delete_product(product_id: UUID) -> bool:
    for index, product in enumerate(products_db):
        if(product.id == product_id):
            products_db.pop(index)
            return True
    return False