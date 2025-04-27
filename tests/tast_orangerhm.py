from pages.loging_page import LoginPage
from pages.dashbord_page import DashboardPage
from pages.leave_page import LeavePage
import time

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

def test_home_page_title(browser):
    browser.get(base_url)
    assert "OrangeHRM" in browser.title

def test_login(browser):
    browser.get(base_url)
    login_page = LoginPage(browser)
    login_page.login(username, password)
    time.sleep(3)
    dashboard = DashboardPage(browser)
    assert dashboard.is_dashboard_displayed()

def test_my_leave(browser):
    browser.get(base_url)
    LoginPage(browser).login(username, password)
    time.sleep(3)
    dashboard = DashboardPage(browser)
    dashboard.click_my_leave()
    time.sleep(3)
    leave_page = LeavePage(browser)
    assert leave_page.is_leave_page_displayed()

def test_logout(browser):
    browser.get(base_url)
    LoginPage(browser).login(username, password)
    time.sleep(3)
    browser.find_element("class name", "oxd-userdropdown-name").click()
    time.sleep(1)
    browser.find_element("xpath", "//a[text()='Logout']").click()
    time.sleep(2)
    assert "login" in browser.current_url.lower()
