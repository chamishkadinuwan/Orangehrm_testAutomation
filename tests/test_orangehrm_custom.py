from pages.login_screen import LoginScreen
from pages.main_dashboard import MainDashboard
from pages.leave_section import LeaveSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
user = "Admin"
pwd = "admin123"

def test_page_title(setup_browser):
    setup_browser.get(url)
    assert "OrangeHRM" in setup_browser.title

def test_user_login(setup_browser):
    setup_browser.get(url)
    login = LoginScreen(setup_browser)
    login.do_login(user, pwd)

    dashboard = MainDashboard(setup_browser)
    WebDriverWait(setup_browser, 10).until(lambda d: dashboard.is_dashboard_visible())
    assert dashboard.is_dashboard_visible()

def test_navigate_my_leave(setup_browser):
    setup_browser.get(url)
    LoginScreen(setup_browser).do_login(user, pwd)

    dash = MainDashboard(setup_browser)
    dash.open_my_leave()

    leave = LeaveSection(setup_browser)
    WebDriverWait(setup_browser, 10).until(lambda d: leave.is_leave_section_visible())
    assert leave.is_leave_section_visible()

def test_user_logout(setup_browser):
    setup_browser.get(url)
    LoginScreen(setup_browser).do_login(user, pwd)

    WebDriverWait(setup_browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))).click()
    WebDriverWait(setup_browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

    WebDriverWait(setup_browser, 10).until(lambda d: "login" in d.current_url.lower())
    assert "login" in setup_browser.current_url.lower()
