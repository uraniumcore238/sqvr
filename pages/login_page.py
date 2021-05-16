import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    LOGIN_PAGE_TITLE=(By.XPATH, "//h1[.='Authentication']")
    CREATE_AN_ACCOUNT_EMAIL = (By.CSS_SELECTOR, "input#email_create")
    EXIST_AN_ACCOUNT_EMAIL=(By.CSS_SELECTOR, "input#email")
    EXIST_AN_ACCOUNT_PASSWORD=(By.CSS_SELECTOR, "input#passwd")
    CREATE_AN_ACCOUNT_BTN=(By.CSS_SELECTOR, "button#SubmitCreate")
    SIGN_IN_BTN=(By.CSS_SELECTOR, "button#SubmitLogin")


    with allure.step("Проверка что страница авторизации открыта"):
        def assert_the_login_page_header(self):
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(LoginPage.LOGIN_PAGE_TITLE))

    with allure.step("Авторизация пользователя"):
        def login_as_user(self, email, password):
            self.driver.find_element(*LoginPage.EXIST_AN_ACCOUNT_EMAIL).send_keys(email)
            self.driver.find_element(*LoginPage.EXIST_AN_ACCOUNT_PASSWORD).send_keys(password)
            self.driver.find_element(*LoginPage.SIGN_IN_BTN).click()

    with allure.step("Регистрация нового пользователя"):
        def new_user_registration(self):
            fake=Faker()
            self.driver.find_element(*LoginPage.CREATE_AN_ACCOUNT_EMAIL).send_keys(fake.ascii_email())
            self.driver.find_element(*LoginPage.CREATE_AN_ACCOUNT_BTN).click()
