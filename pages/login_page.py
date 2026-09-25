from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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
        element = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        )

        # Scroll the button into the visible viewport.
        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        # Move the mouse to the element before clicking.
        # This makes the interaction more reliable in headless Chrome.
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        ActionChains(self.driver) \
            .move_to_element(button) \
            .click() \
            .perform()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE)
        ).text