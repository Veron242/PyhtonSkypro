from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

placeholder_field = driver.find_element(By.ID, "newButtonName")
placeholder_field.send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
blue_button.click()

print(blue_button.text)

driver.quit()
