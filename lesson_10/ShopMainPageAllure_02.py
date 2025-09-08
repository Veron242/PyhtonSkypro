import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открытие страницы магазина")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя {username}")
    def login(self, username, password):
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    @allure.step("Добавление товара {product_name} в корзину")
    def add_product(self, product_name):
        item_xpath = f"//div[contains(text(), '{product_name}')]/ancestor::div[contains(@class, 'inventory_item')]//button"
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
        add_button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()

    @allure.step("Начало оформления заказа")
    def go_to_checkout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

    @allure.step("Заполнение формы оформления заказа")
    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    @allure.step("Получение итоговой суммы заказа")
    def return_sum(self):
        total_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return total_element.text
