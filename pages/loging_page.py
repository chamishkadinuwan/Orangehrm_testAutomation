from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds

        # Wait for the username field to appear
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
