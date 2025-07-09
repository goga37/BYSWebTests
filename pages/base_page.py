import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePageLocators(object):
    LOGO_BUTTON = (By.XPATH, '//*[@id="nohook_logo_link"]')
    VK_SERVICE = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    SEARCH_WRAPPER = (By.XPATH, '//*[@name="st.query"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')

class BasepageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step("Проверяем корректность загрузки скроллбара"):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.VK_SERVICE)
        self.find_element(BasePageLocators.SEARCH_WRAPPER)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}")


    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message=f"Не удалось найти элемент {locator}")

    @allure.step(f'Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step(f'Нажимаеи кнопку экосистемы')
    def click_vk_service(self):
        self.find_element(BasePageLocators.VK_SERVICE).click()
        self.attach_screenshot()

    @allure.step(f'Нажимаеи кнопку еще')
    def click_more_button(self):
        self.attach_screenshot()
        self.find_element(BasePageLocators.MORE_BUTTON).click()

    def get_windows_id(self, index):
        with allure.step(f"Получаем ID окна с индексом {index}"):
            return self.driver.window_handles[index]

    def switch_window(self, window_id):
        with allure.step(f"Переключаемся на окно с ID {window_id}"):
            self.driver.switch_to.window(window_id)