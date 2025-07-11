import allure
from core.base_test import browser
from pages.base_page import BasepageHelper
from pages.login_page import LoginPageHelper
from pages.registration_page import RegistrationPageHelpe

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка регистрации")
@allure.title("Проверка, что в поле телефона подставлен соответствующий код с выбранной страной")
def test_regictration_random_country(browser):
    BasepageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_registration()
    registration_page = RegistrationPageHelpe(browser)
    selected_country_code = registration_page.select_random_country()
    actual_country_code = registration_page.get_phone_field_value()
    with allure.step("Проверка, что в поле телефона подставлен соответствующий код с выбранной страной"):
        assert selected_country_code == actual_country_code
