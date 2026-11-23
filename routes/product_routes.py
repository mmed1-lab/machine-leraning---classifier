
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID

from models.Product import Product
from models.Comment import Comment
from service.product_service import ProductService


router = APIRouter(prefix="/products", tags=["Products"])

# Shared service instance
productService = ProductService()


# Request schemas
class ProductCreate(BaseModel):
    name: str
    price: float


class CommentCreate(BaseModel):
    message: str


# 1. Add a product
@router.post("/", response_model=Product, status_code=201)
def add_product(data: ProductCreate):

    product = Product(
        name=data.name,
        price=data.price
    )

    return productService.addProduct(product)


# 2. Get all products
@router.get("/", response_model=list[Product])
def get_all_products():

    return productService.getProducts()


# 3. Get comments of a product
@router.get("/{prodId}/comments", response_model=list[Comment])
def get_product_comments(prodId: UUID):

    try:
        return productService.selectCommentProduct(prodId)

    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {prodId} not found"
        )


# 4. Add a comment to a product
@router.post("/{prodId}/comments", response_model=Comment, status_code=201)
def add_product_comment(prodId: UUID, data: CommentCreate):

    try:
        return productService.addCommentProduct(
            prodId,
            data.message
        )

    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {prodId} not found"
        )
