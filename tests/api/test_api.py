import pytest
import time


@pytest.mark.api
def test_health_endpoint(api_client):
    response = api_client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.api
def test_login_api_success(api_client):
    response = api_client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "Test@123"
        }
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Login successful"
    assert body["token"]
    assert body["user"]["email"] == "test@example.com"


@pytest.mark.api
@pytest.mark.parametrize(
    "email, password",
    [
        ("test@example.com", "WrongPassword"),
        ("wrong@example.com", "Test@123"),
        ("wrong@example.com", "WrongPassword"),
        ("", "Test@123"),
        ("test@example.com", ""),
    ],
    ids=[
        "wrong_password",
        "wrong_email",
        "wrong_email_and_password",
        "empty_email",
        "empty_password",
    ],
)
def test_login_api_negative(api_client, email, password):
    response = api_client.post(
        "/login",
        json={
            "email": email,
            "password": password
        }
    )

    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"


@pytest.mark.api
def test_login_api_empty_body(api_client):
    response = api_client.post("/login", json={})

    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"


@pytest.mark.api
def test_products_api(api_client):
    response = api_client.get("/products")

    assert response.status_code == 200

    products = response.json()

    assert isinstance(products, list)
    assert len(products) >= 3


@pytest.mark.api
def test_products_have_required_fields(api_client):
    response = api_client.get("/products")

    assert response.status_code == 200

    products = response.json()

    for product in products:
        assert "id" in product
        assert "name" in product
        assert "price" in product


@pytest.mark.api
def test_products_data_types(api_client):
    response = api_client.get("/products")

    assert response.status_code == 200

    products = response.json()

    for product in products:
        assert isinstance(product["id"], int)
        assert isinstance(product["name"], str)
        assert isinstance(product["price"], (int, float))


@pytest.mark.api
def test_products_response_time(api_client):
    start_time = time.perf_counter()

    response = api_client.get("/products")

    response_time = time.perf_counter() - start_time

    assert response.status_code == 200
    assert response_time < 2