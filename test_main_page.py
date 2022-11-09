import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # переходим на страницу логина
    page.go_to_login_page()
    # берем текущий url
    link = browser.current_url
    # создаем объект
    login_page = LoginPage(browser, link)
    # проверяем, что страница загрузилась
    login_page.should_be_login_page()
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    # открываем страницу товара
    page.open()
      # проверяем что есть ссылка на логин
    page.should_be_login_link()
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    # открываем страницу товара
    page.open()
    # открываем корзину
    # page.view_basket()
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser,browser.current_url)
    # проверяем, что перешли на страницу корзины
    basket_page.should_be_basket_page()
    # # Ожидаем, что есть текст о том, что корзина пуста
    basket_page.should_be_text_about_empty_basket()
