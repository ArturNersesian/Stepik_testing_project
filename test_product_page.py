import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    # открываем страницу товара
    page.open()
    # считываем имя товара на странице товара
    name_of_product_at_product_page = page.get_name_of_product()
    # считываем имя цену товара на странице товара
    price_of_product_at_product_page = page.get_price_of_product()
    # добавляем товар в корзину
    page.add_product_to_basket()

    # получаем проверочный код
    page.solve_quiz_and_get_code()
    page.view_basket()
    # проверяем, что цена и название товара на странице товара совпадают с ценой товара и его названием после добавления в корзину
    # page.product_with_correct_name_and_price_should_be_added(name_of_product_at_product_page,price_of_product_at_product_page)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    # открываем страницу товара
    page.open()
    # добавляем товар в корзину
    page.add_product_to_basket()
    #проверяем , что нет сообщения об успещном добавлении
    page.should_not_be_success_message()
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    # открываем страницу товара
    page.open()
    # проверяем , что нет сообщения об успещном добавлении
    page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    # открываем страницу товара
    page.open()
    # добавляем товар в корзину
    page.add_product_to_basket()
    # проверяем , что нет сообщения исчезает
    page.should_disappear_success_message()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # проверяем, что присутствует ссылка на авторизацию
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    # открываем страницу товара
    page.open()
    page.should_be_login_link()
    # переходим на страницу авторизации
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    # проверяем, что открылась страница авторизации
    login_page.should_be_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    # открываем страницу товара
    page.open()
    # открываем корзину
    page.go_to_basket_page()
    # page.view_basket()
    # Ожидаем, что в корзине нет товаров
    page.check_no_products_in_basket()
    # # Ожидаем, что есть текст о том, что корзина пуста
    page.should_be_text_about_empty_basket()

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        # time.sleep(3)
        page = LoginPage(browser, link)
        # открываем страницу авторизации
        page.open()
        # генерируем логин и пароль для регистрации пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "testpass1234"
        # регистрируем нового пользователя
        page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
        page2 = ProductPage(browser,link)
        # открываем страницу товара
        page2.open()
        # проверяем , что нет сообщения об успещном добавлении
        page2.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link2 ="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page2 = ProductPage(browser, link2)
        #открываем страницу товара
        page2.open()
        # time.sleep(3)
        # считываем имя товара на странице товара
        name = page2.get_name_of_product()
        # считываем имя цену товара на странице товара
        price = page2.get_price_of_product()
        # добавляем товар в корзину
        page2.add_product_to_basket()
        # проверяем, что цена и название товара на странице товара совпадают с ценой товара и его названием после добавления в корзину
        page2.product_with_correct_name_and_price_should_be_added(name,price)
#
#
#
#
#
#













