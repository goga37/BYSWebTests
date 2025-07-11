import allure
from core.base_test import browser
from pages.base_page import BasepageHelper
from pages.login_page import LoginPageHelper, LoginPageLocators
from pages.recovery_page import RecoveryPageHelpe

BASE_URL = "https://ok.ru/"
LOGIN_TEXT = "eewqrtty"
PASSWORD_TEXT = "121"

@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода к восстановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasepageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.set_login(LOGIN_TEXT)
    for i in range(3):
        login_page.set_password(PASSWORD_TEXT)
        login_page.click_login_button()

    login_page.click_recovery()
    RecoveryPageHelpe(browser)