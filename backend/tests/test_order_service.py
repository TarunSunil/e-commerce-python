from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from app.models import CartItem, Product
from app.schemas.order import ShippingAddress
from app.services.order_service import create_order


ADDRESS = ShippingAddress(
    address="1 Main Street",
    city="Mumbai",
    state="MH",
    zipCode="400001",
)


class FakeQuery:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def filter(self, *_args):
        return self

    def order_by(self, *_args):
        return self

    def with_for_update(self):
        self.session.lock.acquire()
        self.session.lock_held = True
        return self

    def all(self):
        if self.model is CartItem:
            return [self.session.cart_item]
        return [self.session.product]

    def delete(self):
        return 0


class FakeSession:
    def __init__(self, product, cart_item):
        self.product = product
        self.cart_item = cart_item
        self.lock = Lock()
        self.lock_held = False

    def query(self, model):
        return FakeQuery(self, model)

    def add(self, _value):
        return None

    def commit(self):
        if self.lock_held:
            self.lock_held = False
            self.lock.release()

    def rollback(self):
        if self.lock_held:
            self.lock_held = False
            self.lock.release()

    def refresh(self, _value):
        return None


def make_session(price=10, stock=1):
    product = SimpleNamespace(id="p1", name="Demo product", price=price, stock=stock)
    cart_item = SimpleNamespace(product_id="p1", quantity=1, price=price)
    return FakeSession(product, cart_item)


def test_price_change_returns_409():
    session = make_session(price=12)
    session.cart_item.price = 10

    with pytest.raises(HTTPException) as error:
        create_order(session, "user-1", ADDRESS)

    assert error.value.status_code == 409
    assert error.value.detail["changedLines"][0]["newPrice"] == 12.0


def test_insufficient_stock_is_rejected():
    session = make_session(stock=0)

    with pytest.raises(HTTPException) as error:
        create_order(session, "user-1", ADDRESS)

    assert error.value.status_code == 400
    assert "Insufficient stock" in error.value.detail


def test_concurrent_orders_never_make_stock_negative():
    session = make_session(stock=5)

    def place_order():
        try:
            create_order(session, "user-1", ADDRESS)
            return True
        except HTTPException:
            return False

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(lambda _: place_order(), range(20)))

    assert sum(results) == 5
    assert session.product.stock == 0
    assert session.product.stock >= 0
