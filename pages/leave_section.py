class LeaveSection:
    def __init__(self, driver):
        self.driver = driver

    def is_leave_section_visible(self):
        return "leave" in self.driver.current_url.lower()
