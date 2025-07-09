import allure
from pages.base_page import BasepageHelper
from selenium.webdriver.common.by import By

from pages.recovery_page import RecoveryPageHelpe


class LoginPageLocators():
    LOFIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_CODE = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_QR_CODE_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    REGISTER = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOGIN_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_MAILRU = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    RESTORE_BUTTON = (By.XPATH, '//*[@name="st.go_to_recovery"]')



class LoginPageHelper(BasepageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE)
        self.find_element(LoginPageLocators.RECOVERY_LINK)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE_TAB)
        self.find_element(LoginPageLocators.REGISTER)
        self.find_element(LoginPageLocators.LOGIN_VK)
        self.find_element(LoginPageLocators.LOGIN_MAILRU)
        self.find_element(LoginPageLocators.LOGIN_YANDEX)
        self.find_element(LoginPageLocators.LOFIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login_button(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Ввод логина')
    def set_login(self, login):
        self.find_element(LoginPageLocators.LOFIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Ввод пароля')
    def set_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_MESSAGE).text

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.find_element(LoginPageLocators.RESTORE_BUTTON).click()
        self.attach_screenshot()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER).click()
