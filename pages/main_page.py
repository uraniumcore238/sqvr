import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    MAIN_PAGE_TITLE=(By.XPATH, "//h1[.='Automation Practice Website']")
    SING_IN_BUTTON = (By.CSS_SELECTOR, ".login")

    with allure.step("Проверка что на странице отображается заголовок"):
        def assert_the_header(self):
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(MainPage.MAIN_PAGE_TITLE))

    with allure.step("Переход на страницу авторизации"):
        def go_to_login_page(self):
            self.driver.find_element(*MainPage.SING_IN_BUTTON).click()