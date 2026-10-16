import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    URL = "https://parabank.parasoft.com/parabank/register.htm"

    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM = (By.ID, "repeatedPassword")
    REGISTER_BTN = (By.XPATH, "//input[@value='Register']")

    ERROR_USERNAME = (By.ID, "customer.username.errors")
    ERROR_PASSWORD = (By.ID, "repeatedPassword.errors")
    ERROR_FIRSTNAME = (By.ID, "customer.firstName.errors")
    ERROR_LASTNAME = (By.ID, "customer.lastName.errors")
    ERROR_SSN = (By.ID, "customer.ssn.errors")

    SUCCESS_TITLE = (By.XPATH, "//h1[contains(text(),'Welcome')]")

    @allure.step("Открыть страницу регистрации")
    def open_registration(self):
        self.open(self.URL)
        return self

    @allure.step("Заполнить имя: {value}")
    def fill_first_name(self, value: str):
        self.type(self.FIRST_NAME, value)
        return self

    @allure.step("Заполнить фамилию: {value}")
    def fill_last_name(self, value: str):
        self.type(self.LAST_NAME, value)
        return self

    @allure.step("Заполнить адрес")
    def fill_address(self, value: str):
        self.type(self.ADDRESS, value)
        return self

    @allure.step("Заполнить город")
    def fill_city(self, value: str):
        self.type(self.CITY, value)
        return self

    @allure.step("Заполнить штат")
    def fill_state(self, value: str):
        self.type(self.STATE, value)
        return self

    @allure.step("Заполнить ZIP")
    def fill_zip(self, value: str):
        self.type(self.ZIP, value)
        return self

    @allure.step("Заполнить телефон")
    def fill_phone(self, value: str):
        self.type(self.PHONE, value)
        return self

    @allure.step("Заполнить SSN")
    def fill_ssn(self, value: str):
        self.type(self.SSN, value)
        return self

    @allure.step("Заполнить логин: {value}")
    def fill_username(self, value: str):
        self.type(self.USERNAME, value)
        return self

    @allure.step("Заполнить пароль")
    def fill_password(self, value: str):
        self.type(self.PASSWORD, value)
        return self

    @allure.step("Подтвердить пароль")
    def fill_confirm_password(self, value: str):
        self.type(self.CONFIRM, value)
        return self

    @allure.step("Нажать кнопку Register")
    def click_register(self):
        self.click(self.REGISTER_BTN)
        return self

    @allure.step("Заполнить всю форму регистрации")
    def fill_full_form(self, data: dict):
        self.fill_first_name(data["first_name"])
        self.fill_last_name(data["last_name"])
        self.fill_address(data["address"])
        self.fill_city(data["city"])
        self.fill_state(data["state"])
        self.fill_zip(data["zip"])
        self.fill_phone(data["phone"])
        self.fill_ssn(data["ssn"])
        self.fill_username(data["username"])
        self.fill_password(data["password"])
        self.fill_confirm_password(data["confirm"])
        return self

    @allure.step("Получить текст ошибки логина")
    def get_username_error(self):
        return self.get_text(self.ERROR_USERNAME)

    @allure.step("Получить текст ошибки пароля")
    def get_password_error(self):
        return self.get_text(self.ERROR_PASSWORD)

    @allure.step("Получить текст ошибки имени")
    def get_firstname_error(self):
        return self.get_text(self.ERROR_FIRSTNAME)

    @allure.step("Получить текст ошибки фамилии")
    def get_lastname_error(self):
        return self.get_text(self.ERROR_LASTNAME)

    @allure.step("Получить текст ошибки SSN")
    def get_ssn_error(self):
        return self.get_text(self.ERROR_SSN)

    @allure.step("Проверить, что регистрация успешна")
    def is_registration_successful(self) -> bool:
        return self.is_visible(self.SUCCESS_TITLE, timeout=10)
