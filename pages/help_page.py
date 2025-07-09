import allure
from pages.base_page import BasepageHelper
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class HelpPageLocators():
    HELP_SEARCH_BUTTON = (By.XPATH, '//*[@data-tsid="help_search_input"]')
    TODAY_ACTUAL = (By.XPATH, '//a[contains(@href, "segodnya-aktualno")]')
    REGISTR_YA = (By.XPATH, '//a[contains(@href, "registraciya")]')
    MY_PROFIL = (By.XPATH, '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "obshchenie")]')
    ACCESS_PROFILE = (By.XPATH, '//a[contains(@href, "dostup-k-profilu")]')
    SAFETY = (By.XPATH, '//a[contains(@href, "bezopasnost")]')
    GROUPS = (By.XPATH, '//a[contains(@href, "gruppy")]')
    PAID_FEATURES = (By.XPATH, '//a[contains(@href, "platnye-funkcii")]')
    VIOLATIONS_SPAM = (By.XPATH, '//a[contains(@href, "narusheniya-i-spam")]')
    GAMES_APPS = (By.XPATH, '//a[contains(@href, "igry-i-prilojeniya")]')
    SERVICSE = (By.XPATH, '//a[contains(@href, "drugie-servisy")]')
    USEFUL_INFORMATION = (By.XPATH, '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISING_CABINET = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')


class HelpPageHelper(BasepageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.HELP_SEARCH_BUTTON)
        self.find_element(HelpPageLocators.TODAY_ACTUAL)
        self.find_element(HelpPageLocators.REGISTR_YA)
        self.find_element(HelpPageLocators.MY_PROFIL)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.ACCESS_PROFILE)
        self.find_element(HelpPageLocators.SAFETY)
        self.find_element(HelpPageLocators.VIOLATIONS_SPAM)
        self.find_element(HelpPageLocators.GAMES_APPS)
        self.find_element(HelpPageLocators.SERVICSE)
        self.find_element(HelpPageLocators.USEFUL_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISING_CABINET)
        self.find_element(HelpPageLocators.PAID_FEATURES)
        self.find_element(HelpPageLocators.VIOLATIONS_SPAM)
        self.find_element(HelpPageLocators.GAMES_APPS)
        self.find_element(HelpPageLocators.SERVICSE)
        self.find_element(HelpPageLocators.USEFUL_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISING_CABINET)

    @allure.step('Скролл к элементу')
    def scroll_to_item(self,locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
