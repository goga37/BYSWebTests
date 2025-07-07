import allure
from core.base_test import browser
from pages.advertising_cabinet_page import AdvertisingCabinetPageHelper
from pages.base_page import BasePage
from pages.help_page import HelpPageHelper, HelpPageLocators

BASE_URL = "https://ok.ru/help"

@allure.suite("Проверка страницы помощи")
@allure.title("Проверка перехода в рекламный кабинет")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    help_page = HelpPageHelper(browser)
    help_page.scroll_to_item(HelpPageLocators.ADVERTISING_CABINET)
    AdvertisingCabinetPageHelper(browser)