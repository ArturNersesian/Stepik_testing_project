from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    # открывает страницу переданную в url
    def open(self):
        self.browser.get(self.url)
    # Проверяет присутствует ли элемент на странице (возвращает True или False)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

