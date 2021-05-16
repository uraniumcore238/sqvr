import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyAccountPage():
    def __init__(self, driver):
        self.driver = driver

    ACCOUNT_TITLE=(By.XPATH, "//h1[.='My account']")

    with allure.step("Проверка, что на странице аккаунта пользователя отображается заголовок"):
        def assert_my_account_page_header(self):
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(MyAccountPage.ACCOUNT_TITLE))