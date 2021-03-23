from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from random import randint
from time import sleep


# https://society6.com/pillows
class Pillows:

    #LOCATORS
    _main_header = 'h1[id="title"]' # text "Throw Pillows"