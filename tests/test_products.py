from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "description": "Gaming Laptop",
            "price": 75000,
            "quantity": 10,
            "category": "Electronics"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Laptop"
    assert data["price"] == 75000
    assert data["quantity"] == 10


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product():
    response = client.get("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1


def test_product_not_found():
    response = client.get("/products/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_delete_product():
    response = client.delete("/products/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"
