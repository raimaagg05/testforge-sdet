import pytest

from utils.db_utils import fetch_one, fetch_all


@pytest.mark.db
def test_test_user_exists(db_path):
    user = fetch_one(
        db_path,
        "SELECT email FROM users WHERE email=?",
        ("test@example.com",)
    )

    assert user is not None
    assert user[0] == "test@example.com"


@pytest.mark.db
def test_user_email_is_valid(db_path):
    user = fetch_one(
        db_path,
        "SELECT email FROM users WHERE email=?",
        ("test@example.com",)
    )

    assert user is not None
    assert "@" in user[0]
    assert "." in user[0]


@pytest.mark.db
def test_user_password_exists(db_path):
    user = fetch_one(
        db_path,
        "SELECT password FROM users WHERE email=?",
        ("test@example.com",)
    )

    assert user is not None
    assert user[0] != ""


@pytest.mark.db
def test_products_exist(db_path):
    products = fetch_all(
        db_path,
        "SELECT name, price FROM products ORDER BY id"
    )

    assert len(products) >= 3
    assert all(name for name, price in products)
    assert all(price > 0 for name, price in products)


@pytest.mark.db
def test_product_count(db_path):
    result = fetch_one(
        db_path,
        "SELECT COUNT(*) FROM products"
    )

    assert result is not None
    assert result[0] >= 3


@pytest.mark.db
def test_product_ids_are_unique(db_path):
    products = fetch_all(
        db_path,
        "SELECT id FROM products"
    )

    ids = [product[0] for product in products]

    assert len(ids) == len(set(ids))


@pytest.mark.db
def test_product_names_are_not_empty(db_path):
    products = fetch_all(
        db_path,
        "SELECT name FROM products"
    )

    assert len(products) >= 3
    assert all(product[0].strip() for product in products)


@pytest.mark.db
def test_product_prices_are_positive(db_path):
    products = fetch_all(
        db_path,
        "SELECT price FROM products"
    )

    assert len(products) >= 3
    assert all(product[0] > 0 for product in products)