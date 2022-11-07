import time
from .pages.main_page import MainPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# def test_add_to_busket_buton_exists(browser):
#     browser.get(link)
#     browser.implicitly_wait(10)
#
#     assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Кнопка добавления в корзину не найдена"

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()