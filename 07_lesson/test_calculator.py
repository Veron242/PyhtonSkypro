from selenium import webdriver
from calculator_page import CalculatorPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def test_slow_calculator():
    # Инициализация Chrome WebDriver

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    calculator = CalculatorPage(driver)

    # Установка задержки и выполнение вычисления
    calculator.set_delay("delay")
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # Проверка результата
    calculator.get_result()
    assert result == "15", f"Ожидался результат 15, получено {result}"

    # Закрытие браузера
    driver.quit()

