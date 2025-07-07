import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random


class RegistrationPageLocators:
    PHONE_NUMBER = (By.XPATH, '//*[@id="field_phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//*[@class="country-select_code"]')
    NEXT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    SUPPORT_BUTON = (By.XPATH, '//*[@data-l="t,support"]')
    SELECT_CODE = (By.CLASS_NAME, "country-select_code")


class RegistrationPageHelpe(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_NUMBER)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.NEXT_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_BUTON)

    @allure.step("Выбор случайной страны и получение её кода")
    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        self.attach_screenshot()
        country_code = country_items[random_number].text
        country_items[random_number].click()
        return country_code

    @allure.step("Получение фактического кода страны из поля номер")
    def get_phone_field_value(self):
        self.attach_screenshot()
        return self.find_element(RegistrationPageLocators.PHONE_NUMBER).get_attribute('value')
