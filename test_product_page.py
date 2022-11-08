import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
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
    # проверяем, что цена и название товара на странице товара совпадают с ценой товара и его названием после добавления в корзину
    page.product_with_correct_name_and_price_should_be_added(name_of_product_at_product_page,price_of_product_at_product_page)

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     # открываем страницу товара
#     page.open()
#     # добавляем товар в корзину
#     page.add_product_to_basket()
#     #проверяем , что нет сообщения об успещном добавлении
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     # открываем страницу товара
#     page.open()
#     # проверяем , что нет сообщения об успещном добавлении
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     # открываем страницу товара
#     page.open()
#     # добавляем товар в корзину
#     page.add_product_to_basket()
#     # проверяем , что нет сообщения исчезает
#     page.should_disappear_success_message()