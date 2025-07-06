import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RecoveryPageLocators():
    PHONE_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    QR_CODE = (By.XPATH, '//*[@class="qr_code_image"]')
    SUPPORT_BUTON = (By.XPATH, '//*[@data-l="t,support"]')


class RecoveryPageHelpe(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTON)