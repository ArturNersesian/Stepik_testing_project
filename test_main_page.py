import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_busket_buton_exists(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Кнопка добавления в корзину не найдена"


