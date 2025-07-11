import allure
from pages.base_page import BasepageHelper
from selenium.webdriver.common.by import By

class VkEcosystemPageLocators:
    TITLE = (By.XPATH, '//*[@class="title-h2"]')


class VkEcosystemPageHelpe(BasepageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.find_element(VkEcosystemPageLocators.TITLE).click()
            self.attach_screenshot()