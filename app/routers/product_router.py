from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID
from app.models.product_model import Product
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
async def get_products():
    return product_service.get_all_products()

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: UUID):
    product = product_service.get_product_by_uuid(product_id)
    if not product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Product)
async def create_product(product: Product):
    return product_service.create_product(product)

# --- PUT (Update) ---
@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: UUID, product: Product):
    result = product_service.update_product(product_id, product)
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Producto no encontrado para actualizar")
    return result

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID):
    success = product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Producto no encontrado para eliminar")
    return None