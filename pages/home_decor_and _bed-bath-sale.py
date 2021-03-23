from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from random import randint
from time import sleep


# https://society6.com/collection/home-decor-and-bed-bath-sale
class HomeDecorAndBedBathSale:

    #LOCATORS
    _pop_up_close = 'a[data-click="close"]'
    _top_block_text = '//div[contains(@class,"titleBlockWrapCenter")]//h1'