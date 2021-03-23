
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_homepage(self):
        self.driver.get("https://society6.com?123")
        self.driver.maximize_window()
