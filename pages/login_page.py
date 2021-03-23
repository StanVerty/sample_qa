from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


# https://society6.com/
class LoginPage(BasePage):

    #LOCATORS
    _login_button = 'div[id="nav-login"] a'
    _email = 'input[id="top-email"]'
    _password = 'input[id="top-password"]'
    _signin_button = 'button[id="ml-login-submit"]'
    _nav_user_trigger = 'a[id="nav_user_menu-trigger"]'
    _user_name = 'a[id="nav-username"]'
    _signout_button = 'a[id="mn-logout"]'


    def set_user_name(self, username):
        loginLink = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self._login_button)))
        actions = ActionChains(self.driver)
        actions.move_to_element(loginLink).perform()
        sleep(2)
        emailField = self.driver.find_element(By.CSS_SELECTOR, self._email)
        emailField.clear()
        emailField.send_keys(username)

    def set_password(self, password):
        passwordField = self.driver.find_element(By.CSS_SELECTOR, self._password)
        passwordField.clear()
        passwordField.send_keys(password)

    def click_signin(self):
        signinButton = self.driver.find_element(By.CSS_SELECTOR, self._signin_button)
        signinButton.click()

    def user_name(self):
        try:
            userLink = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._nav_user_trigger)))
            actions = ActionChains(self.driver)
            actions.move_to_element(userLink).perform()
            sleep(3)
            user_name = self.driver.find_element(By.CSS_SELECTOR, self._user_name)
            print(user_name.text)
            return user_name.text
        except NoSuchElementException:
            return ""

    def click_signout(self):
        signout_link = self.driver.find_element(By.CSS_SELECTOR, self._nav_user_trigger)
        actions = ActionChains(self.driver)
        actions.move_to_element(signout_link).perform()
        self.driver.find_element(By.CSS_SELECTOR, self._signin_button).click()
