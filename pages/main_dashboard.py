from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainDashboard:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_visible(self):
        return "dashboard" in self.driver.current_url.lower()

    def open_my_leave(self):
        wait = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']"))
            ).click()


