from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    LIST_OF_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")

    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :first-child div strong")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(3) div strong")
    # NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    # PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-1 p")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3) div strong")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    LIST_OF_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4")
class BasketPageLocators():
    LIST_OF_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")