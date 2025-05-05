from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def do_login(self, user, pwd):
        wait = WebDriverWait(self.driver, 10)
        user_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        pass_field = self.driver.find_element(By.NAME, "password")
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        user_field.send_keys(user)
        pass_field.send_keys(pwd)
        submit_btn.click()
