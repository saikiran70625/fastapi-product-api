from fastapi import FastAPI, HTTPException
from app.schemas import Product, ProductCreate

app = FastAPI(title="Product REST API")

products = []
product_id = 1


@app.get("/products", response_model=list[Product])
def get_products():
    return products


@app.get("/products/{id}", response_model=Product)
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    global product_id

    new_product = Product(
        id=product_id,
        **product.model_dump()
    )

    products.append(new_product)
    product_id += 1

    return new_product


@app.delete("/products/{id}")
def delete_product(id: int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return {"message": "Product deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
