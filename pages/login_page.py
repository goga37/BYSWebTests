from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOFIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_CODE = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_link = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_QR_CODE_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    REGISTER = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOGIN_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_MAILRU = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE)
        self.find_element(LoginPageLocators.RECOVERY_link)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE_TAB)
        self.find_element(LoginPageLocators.REGISTER)
        self.find_element(LoginPageLocators.LOGIN_VK)
        self.find_element(LoginPageLocators.LOGIN_MAILRU)
        self.find_element(LoginPageLocators.LOGIN_YANDEX)
        self.find_element(LoginPageLocators.LOFIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)

    def click_login_button(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.find_element(LoginPageLocators.LOFIN_FIELD).send_keys(login)

    def set_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_MESSAGE).text