import allure
from data.data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage
from utilities.BaseClass import BaseClass


class TestUserAuthorization(BaseClass):

    @allure.feature('Аллюр фича')
    @allure.story('Аллюр стори')
    @allure.severity('critical')
    def test_assert_the_main_page(self):

        with allure.step("Авторизация зарегистрированным пользователем на сайте 'http://automationpractice.com'"):
            data_test = Data()

            mainPage = MainPage(self.driver)
            loginPage=LoginPage(self.driver)
            myAccountPage=MyAccountPage(self.driver)

            with allure.step("Открытие главной страницы сайта"):
                mainPage.assert_the_header()
            with allure.step("Переход на страницу выбора логина или регистрации"):
                mainPage.go_to_login_page()
                loginPage.assert_the_login_page_header()
            with allure.step("Переход на страницу личного аккаунта"):
                loginPage.login_as_user(data_test.exising_user_email, data_test.exising_user_password)
            with allure.step("Проверка, что авторизация пользователя прошла успешно"):
                myAccountPage.assert_my_account_page_header()

