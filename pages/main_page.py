from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def view_basket(self):
    #     login_link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
    #     login_link.click()


