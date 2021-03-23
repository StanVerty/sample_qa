import pytest
from pages.login_page import LoginPage


@pytest.mark.login
class LoginTest():
        username = "stan.vertii@gmail.com"
        password = "123123"

        # driver.maximize_window()

        def test_valid_login(self, driver):
            lp = LoginPage(driver)
            lp.go_to_homepage()
            lp.set_user_name(self.username)
            lp.set_password(self.password)
            lp.click_signin()

            assert lp.user_name() == "Stan_V"
