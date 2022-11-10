from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"подстроки login нет в {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.CSS_SELECTOR, '[type="email"][name="registration-email"]')
        email_input.send_keys(email)

        pass_input1 = self.browser.find_element(By.CSS_SELECTOR, '[type="password"][name="registration-password1"]')
        pass_input1.send_keys(password)

        pass_input1 = self.browser.find_element(By.CSS_SELECTOR, '[type="password"][name="registration-password2"]')
        pass_input1.send_keys(password)

        register_button = self.browser.find_element(By.CSS_SELECTOR,'[name = "registration_submit"]')
        register_button.click()

    def should_be_text_about_registration(self):
        # assert self.is_element_present(*ProductPageLocators.EMPTY_BASKET_MESSAGE)
        text = self.browser.find_element(By.CSS_SELECTOR,".alert-success .alertinner.wicon").text
        assert text == "Thanks for registering!"



