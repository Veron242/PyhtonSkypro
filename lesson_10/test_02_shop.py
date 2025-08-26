import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ShopMainPageAllure import SauceDemoPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.epic("Магазин одежды")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка оформления покупки в магазине saucedemo")
@allure.description("Тест проверяет корректность оформления покупки товаров в магазине одежды")

def test_sauce_demo_purchase(driver):
    with allure.step("Инициализация страницы магазина"):
        shop = SauceDemoPage(driver)
    with allure.step("Авторизация на сайте"):
        shop.login("standard_user", "secret_sauce")
    with allure.step("Добавление товаров в корзину"):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item in items_to_add:
            with allure.step(f"Добавление товара: {item}"):
                shop.add_product(item)

    with allure.step("Переход в корзину"):
        shop.go_to_cart()

    with allure.step("Начало оформления заказа"):
        shop.go_to_checkout()

    with allure.step("Заполнение данных доставки"):
        shop.fill_checkout_form("Вероника", "Константинова", "188680")

    with allure.step("Проверка итоговой суммы"):
        total_text = shop.return_sum()

    with allure.step(f"Проверить что сумма {total_text} равна 'Total: $58.29'"):
         assert total_text == "Total: $58.29", f"Итоговая сумма {total_text} не соответствует ожидаемой $58.29"
