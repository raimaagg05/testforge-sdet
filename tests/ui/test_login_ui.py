import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.parametrize(
    "email, password, expected_message",
    [
        ("test@example.com", "Test@123", "Login successful"),
        ("test@example.com", "WrongPassword", "Invalid credentials"),
        ("wrong@example.com", "Test@123", "Invalid credentials"),
        ("wrong@example.com", "WrongPassword", "Invalid credentials"),
        ("", "Test@123", "Email and password are required"),
        ("test@example.com", "", "Email and password are required"),
        ("", "", "Email and password are required"),
    ],
    ids=[
        "valid_credentials",
        "wrong_password",
        "wrong_email",
        "wrong_email_and_password",
        "empty_email",
        "empty_password",
        "empty_credentials",
    ],
)
def test_login_scenarios(driver, base_url, email, password, expected_message):
    page = LoginPage(driver)

    page.open(base_url)
    page.login(email, password)

    assert page.get_message() == expected_message