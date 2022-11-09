from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    def view_basket(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        login_link.click()

    def should_be_login_link(self):
       assert self.browser.find_element(*BasePageLocators.LOGIN_LINK)
