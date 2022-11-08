from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")

    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :first-child div strong")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(3) div strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3) div strong")