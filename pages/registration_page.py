from random import randint
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker


class RegistrationPage():
    def __init__(self, driver):
        self.driver = driver

    REGISTRATION_PAGE_TITLE = (By.XPATH, "//h1[.='Create an account']")
    TILLE_RADIO_BUTTON = (By.CSS_SELECTOR, ".radio-inline")
    FIRST_CUST_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#customer_firstname")
    LAST_CUST_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#customer_lastname")
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#passwd")
    DAY_OF_BIRTH = (By.CSS_SELECTOR, "#days")
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, "#months")
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, "#years")
    FIRST_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#lastname")
    COMPANY_NAME_INPUT_FIELD = (By.CSS_SELECTOR, "#company")
    ADDRESS_INPUT_FIELD = (By.CSS_SELECTOR, "#address1")
    ADDRESS_TWO_INPUT_FIELD = (By.CSS_SELECTOR, "#address2")
    CITY_INPUT_FIELD = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#id_state")
    ALL_STATES = (By.CSS_SELECTOR, "#id_state option[value='1']")
    ZIP_CODE_INPUT_FIELD = (By.CSS_SELECTOR, "#postcode")
    COUNTRY = (By.CSS_SELECTOR, "#id_country")
    ADDITIONAL_INFORMATION_INPUT_FIELD = (By.CSS_SELECTOR, "#other")
    HOME_PHONE_INPUT_FIELD = (By.CSS_SELECTOR, "#phone")
    MOBILE_PHONE_INPUT_FIELD = (By.CSS_SELECTOR, "#phone_mobile")
    ASSIGN_AN_ADDRESS_INPUT_FIELD = (By.CSS_SELECTOR, "#alias")
    REGISTER_BTN = (By.CSS_SELECTOR, "#submitAccount")

    with allure.step("Проверка что страница регистрации открыта"):
        def assert_the_registration_page_header(self):
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(RegistrationPage.REGISTRATION_PAGE_TITLE))

    with allure.step("Заполнение формы регистрации нового пользователя"):
        def fill_all_fields_in_reg_form(self):
            fake = Faker()
            f_password=fake.password(length=9, special_chars=False, digits=True, upper_case=True, lower_case=True)
            f_first_name = fake.first_name()
            f_last_name=fake.last_name()
            f_address=fake.address()
            state_number = randint(1, 50)
            day_number = randint(1, 31)
            month_number = randint(1, 12)
            year_number = randint(1900, 2021)
            mr_or_mrs=randint(1, 2)

            with allure.step("Нажатие на радио кнопку выбора типа обращения 'Mr/Mrs' пользователя"):
                self.driver.find_element_by_css_selector(f"label[for='id_gender{mr_or_mrs}']").click()
            with allure.step("Заполнение полей Имя и Фамилия"):
                self.driver.find_element(*RegistrationPage.FIRST_CUST_NAME_INPUT_FIELD).send_keys(f_first_name)
                self.driver.find_element(*RegistrationPage.LAST_CUST_NAME_INPUT_FIELD).send_keys(f_last_name)
            with allure.step("Заполнение полей даты рождения день, месяц, год"):
                self.driver.find_element(*RegistrationPage.DAY_OF_BIRTH).click()
                self.driver.find_element_by_css_selector(f"#days option[value='{day_number}']").click()
                self.driver.find_element(*RegistrationPage.MONTH_OF_BIRTH).click()
                self.driver.find_element_by_css_selector(f"#months option[value='{month_number}']").click()
                self.driver.find_element(*RegistrationPage.YEAR_OF_BIRTH).click()
                self.driver.find_element_by_css_selector(f"#years option[value='{year_number}']").click()
            with allure.step("Заполнение полей названия компании и адреса"):
                self.driver.find_element(*RegistrationPage.COMPANY_NAME_INPUT_FIELD).send_keys(fake.company())
                self.driver.find_element(*RegistrationPage.ADDRESS_INPUT_FIELD).send_keys(f_address)
            with allure.step("Заполнение поля названия города"):
                self.driver.find_element(*RegistrationPage.CITY_INPUT_FIELD).send_keys(fake.city())
            with allure.step("Заполнение поля почтового кода"):
                self.driver.find_element(*RegistrationPage.ZIP_CODE_INPUT_FIELD).send_keys(fake.postcode())
            with allure.step("Заполнение поля 'Дополнительная информация'"):
                self.driver.find_element(*RegistrationPage.ADDITIONAL_INFORMATION_INPUT_FIELD).send_keys(f_address)
            with allure.step("Заполнение поля номера мобильного телефона"):
                self.driver.find_element(*RegistrationPage.MOBILE_PHONE_INPUT_FIELD).send_keys(fake.msisdn())
            with allure.step("Выбор рандомного штата в селкторе выбора"):
                self.driver.find_element(*RegistrationPage.STATE).click()
                self.driver.find_element_by_css_selector(f"#id_state option[value='{state_number}']").click()
            with allure.step("Заполнения поля 'Assign an address alias for future reference'"):
                self.driver.find_element(*RegistrationPage.ASSIGN_AN_ADDRESS_INPUT_FIELD).send_keys(fake.phone_number())
            with allure.step("Заполнения поля пароля"):
                self.driver.find_element(*RegistrationPage.PASSWORD_INPUT_FIELD).click()
                self.driver.find_element(*RegistrationPage.PASSWORD_INPUT_FIELD).send_keys(f_password)
            with allure.step("Нажатие на кнопку 'Register'"):
                self.driver.find_element(*RegistrationPage.REGISTER_BTN).click()