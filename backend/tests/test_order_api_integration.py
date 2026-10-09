import uuid

from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models import CartItem, Order, Product, User


def test_order_and_cart_api_contract_against_postgres():
    email = f"order-contract-{uuid.uuid4()}@example.com"
    client = TestClient(app)
    db = SessionLocal()
    product = Product(
        name="Contract test product",
        description="Product used for API contract testing",
        categories=["test"],
        price=19.99,
        images=["https://example.com/product.webp"],
        stock=4,
        attributes={},
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    try:
        register = client.post(
            "/api/auth/register",
            json={"name": "Order Contract User", "email": email, "password": "correct horse"},
        )
        assert register.status_code == 200
        token = register.json()["token"]
        user_id = register.json()["userId"]
        headers = {"Authorization": f"Bearer {token}"}

        add_to_cart = client.post(
            "/api/cart",
            headers=headers,
            json={"productId": product.id, "quantity": 2},
        )
        assert add_to_cart.status_code == 200

        cart = client.get("/api/cart", headers=headers)
        assert cart.status_code == 200
        cart_item = cart.json()[0]
        assert set(cart_item) == {
            "id",
            "userId",
            "productId",
            "quantity",
            "price",
            "productName",
            "productImage",
            "stock",
        }
        assert cart_item["productId"] == product.id
        assert cart_item["productName"] == product.name
        assert isinstance(cart_item["price"], (int, float))
        assert not isinstance(cart_item["price"], bool)

        order_response = client.post(
            "/api/orders",
            headers=headers,
            json={
                "shippingAddress": {
                    "address": "1 Main Street",
                    "city": "Mumbai",
                    "state": "MH",
                    "zipCode": "400001",
                }
            },
        )
        assert order_response.status_code == 200
        order = order_response.json()
        assert set(order) == {"id", "userId", "items", "status", "total", "createdAt", "shippingAddress"}
        assert order["userId"] == user_id
        assert isinstance(order["total"], (int, float))
        assert not isinstance(order["total"], bool)
        assert set(order["items"][0]) == {"productId", "qty", "price", "productName", "unitPrice"}
        assert order["items"][0]["productId"] == product.id
        assert order["items"][0]["productName"] == product.name
        assert isinstance(order["items"][0]["price"], (int, float))
        assert isinstance(order["items"][0]["unitPrice"], (int, float))

        detail = client.get(f"/api/orders/{order['id']}", headers=headers)
        history = client.get(f"/api/orders/user/{user_id}", headers=headers)
        assert detail.status_code == 200
        assert history.status_code == 200
        assert detail.json() == order
        assert history.json()[0] == order
    finally:
        user = db.query(User).filter(User.email == email).first()
        if user:
            db.query(CartItem).filter(CartItem.user_id == user.id).delete()
            db.query(Order).filter(Order.user_id == user.id).delete()
            db.delete(user)
        db.delete(product)
        db.commit()
        db.close()
