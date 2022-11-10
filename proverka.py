from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    time.sleep(3)

    email = str(time.time()) + "@fakemail.org"
    password = "testpass1234"

    email_input = driver.find_element(By.CSS_SELECTOR, '[type="email"][name="registration-email"]')
    email_input.send_keys(email)

    pass_input1 = driver.find_element(By.CSS_SELECTOR, '[type="password"][name="registration-password1"]')
    pass_input1.send_keys(password)

    pass_input1 = driver.find_element(By.CSS_SELECTOR, '[type="password"][name="registration-password2"]')
    pass_input1.send_keys(password)

    register_button = driver.find_element(By.CSS_SELECTOR, '[name = "registration_submit"]')
    register_button.click()

    time.sleep(3)

    driver.get('http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    time.sleep(5)

    name = driver.find_element(By.CSS_SELECTOR, 'div h1').text
    price = driver.find_element(By.CSS_SELECTOR, '.product_main .price_color').text
    print(f"PRICE: {name}")
    print(f"NAME OF PRODUCT: {price}")

    driver.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').click()
    time.sleep(3)

    name_in_basket = driver.find_element(By.CSS_SELECTOR, '#messages :first-child div strong').text
    price_in_basket = driver.find_element(By.CSS_SELECTOR, '#messages :nth-child(3) div strong').text
    print(f"PRICE IN BASKET: {name_in_basket}")
    print(f"NAME OF PRODUCT IN BASKET: {price_in_basket}")


except Exception as ex:
    print(ex)
finally:
    driver.quit()