import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_checkout():
    driver = webdriver.Firefox()  # Запуск Firefox
    driver.get("https://www.saucedemo.com/")

    # Логин
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    items_to_add = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item_description']//button"
        driver.find_element(By.XPATH, item_xpath).click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Начало оформления заказа
    driver.find_element(By.ID, "checkout").click()

   # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Вероника")
    driver.find_element(By.ID, "last-name").send_keys("Константинова")
    driver.find_element(By.ID, "postal-code").send_keys("188680")
    driver.find_element(By.ID, "continue").click()

    # Получение итоговой суммы
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text  # "Total: $58.29"
    total_amount = total_text.split("$")[1]  # "58.29"

    # Проверка суммы
    assert total_amount == "58.29", f"Ожидалось $58.29, но получилось ${total_amount}"

    # Закрытие браузера
    driver.quit()