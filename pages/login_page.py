from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE)
        ).text
