import time

from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    def product_with_correct_name_and_price_should_be_added(self,name_at_product_page,price_at_product_page):
        self.should_have_right_name(name_at_product_page)
        self.should_have_rigth_price(price_at_product_page)

    def should_have_right_name(self,name_at_product_page):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET).text
        print(f"NAME ===== {name_in_basket}")
        assert name_at_product_page in name_in_basket, "Name is not same"
        # assert "The shellcoder's handbook" in name_in_basket, "Login form is not presented"

    def should_have_rigth_price(self,price_at_product_page):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_BASKET).text
        print(f"PRICE ===== {price_in_basket}")
        assert price_at_product_page in price_in_basket, "Name is not same"
        # assert "9.99" in price_in_basket, "Login form is not presented"

    def get_name_of_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        print(f"URL: {self.browser.current_url}")
        print(f"NAME IN PRODUCT PAGE ===== {name}")
        return name

    def get_price_of_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        print(f"PRICE IN PRODUCT PAGE ===== {price}")
        return price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



    def view_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.VIEW_BASKET_BUTTON)
        login_link.click()

    def check_no_products_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.LIST_OF_PRODUCTS_IN_BASKET), \
            "List of products exists, but shouldn't be"

    def should_be_text_about_empty_basket(self):
        # assert self.is_element_present(*ProductPageLocators.EMPTY_BASKET_MESSAGE)
        text = self.browser.find_element(*ProductPageLocators.EMPTY_BASKET_MESSAGE).text
        print(f"MESSAGE IN EMPTY BASKET: {text}")
        assert text == "Your basket is empty. Continue shopping", "No text about empty basket"


