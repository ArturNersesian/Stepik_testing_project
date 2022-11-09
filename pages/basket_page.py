from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators
class   BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "basket" in current_url, f"подстроки basket нет в {current_url}"

    def check_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_PRODUCTS_IN_BASKET), \
            "List of products exists, but shouldn't be"

    def should_be_text_about_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        print(f"MESSAGE IN EMPTY BASKET: {text}")
        assert text == "Your basket is empty. Continue shopping", "No text about empty basket"

    # def should_be_login_form(self):
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    #
    # def should_be_register_form(self):
    #     # реализуйте проверку, что есть форма регистрации на странице
    #     assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"