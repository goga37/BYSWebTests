import allure
from core.base_test import browser
from pages.base_page import BasepageHelper
from pages.login_page import LoginPageHelper
from pages.vk_ecosystem_page import VkEcosystemPageHelpe

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка тулбара")
@allure.title("Переход к проектам экосистемы VK")
def test_go_to_eco_system(browser):
    base_page = BasepageHelper(browser)
    base_page.get_url(BASE_URL)
    base_page.check_page()
    login_page = LoginPageHelper(browser)
    current_window_id = base_page.get_windows_id(0)
    login_page.click_vk_service()
    login_page.click_more_button()
    new_window_id = base_page.get_windows_id(1)
    login_page.switch_window(new_window_id)
    vk_ecosystem = VkEcosystemPageHelpe(browser)
    vk_ecosystem.switch_window(current_window_id)
    LoginPageHelper(browser)