import allure

from pages.base_page import BasepageHelper
from selenium.webdriver.common.by import By

class AdvertisingCabinetPageLocators():
    TITLE = (By.XPATH, '// a[span[text() = "Рекламный кабинет"]]')

class AdvertisingCabinetPageHelper(BasepageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(AdvertisingCabinetPageLocators.TITLE)


