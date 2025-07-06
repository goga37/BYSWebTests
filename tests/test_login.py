import allure
from core.base_test import browser
from pages.base_page import BasePage
from pages.login_page import LoginPageHelper

BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_PASSWORD_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"


@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login_button()
    assert login_page.get_error_text() == EMPTY_LOGIN_PASSWORD_ERROR

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустом пароле")
def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.set_login("igor225")
    login_page.click_login_button()
    assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR
