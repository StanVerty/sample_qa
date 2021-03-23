from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from random import randint
from time import sleep


#https://society6.com/phone-cases
class PhoneCases:

    #LOCATORS
    _main_header = '//div[contains(@class,"titleBlockContainer_heroHeader")]//h1'