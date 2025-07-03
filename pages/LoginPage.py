from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOFIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_CODE = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_link = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_QR_CODE_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    REGISTER = (By.XPATH, '//*[@data-l="t,register"]')
    LOGIN_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_MAILRU = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')


class LoginPageHelper(BasePage):
    pass