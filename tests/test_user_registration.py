import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage
from pages.registration_page import RegistrationPage
from utilities.BaseClass import BaseClass


class TestUserRegistration(BaseClass):

    @allure.feature('Аллюр фича')
    @allure.story('Аллюр стори')
    @allure.severity('critical')
    def test_assert_the_main_page(self):

        with allure.step("Регистрация нового пользователя на сайте 'http://automationpractice.com'"):

            mainPage = MainPage(self.driver)
            loginPage=LoginPage(self.driver)
            myAccountPage=MyAccountPage(self.driver)
            registrationPage = RegistrationPage(self.driver)

            with allure.step("Открытие главной страницы сайта"):
                mainPage.assert_the_header()
            with allure.step("Переход на страницу выбора логина или регистрации"):
                mainPage.go_to_login_page()
                loginPage.assert_the_login_page_header()
            with allure.step("Переход на страницу выбора регистрации/авторизации пользователя"):
                loginPage.new_user_registration()
            with allure.step("Проверка, что переход на страницу регистрации прошел успешно"):
                registrationPage.assert_the_registration_page_header()
            with allure.step("Заполнение формы регистрации и нажатие на кнопку 'Register'"):
                registrationPage.fill_all_fields_in_reg_form()
            with allure.step("Проверка, что регистрация пользователя прошла успешно"):
                myAccountPage.assert_my_account_page_header()

