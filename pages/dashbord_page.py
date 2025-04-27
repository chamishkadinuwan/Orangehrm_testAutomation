from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_displayed(self):
        return "dashboard" in self.driver.current_url.lower()

    def click_my_leave(self):
        wait = WebDriverWait(self.driver, 10)  # wait up to 10 seconds
        my_leave_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Leave']")))
        my_leave_button.click()
