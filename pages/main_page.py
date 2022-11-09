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
    def check_no_products_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.LIST_OF_PRODUCTS_IN_BASKET), \
            "List of products exists, but shouldn't be"

    def should_be_text_about_empty_basket(self):
        text = self.browser.find_element(*MainPageLocators.EMPTY_BASKET_MESSAGE).text
        print(f"MESSAGE IN EMPTY BASKET: {text}")
        assert text == "Your basket is empty. Continue shopping", "No text about empty basket"

    def should_be_login_link(self):
       assert self.browser.find_element(*BasePageLocators.LOGIN_LINK)
