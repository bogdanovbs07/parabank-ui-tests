import time
import allure
import pytest

from pages.registration_page import RegistrationPage


def unique_username(prefix: str = "user") -> str:
    return f"{prefix}{int(time.time() * 1000)}"


VALID_DATA = {
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "address": "Lenina 1",
    "city": "Moscow",
    "state": "MSK",
    "zip": "123456",
    "phone": "89991234567",
    "ssn": "123456789",
    "username": "",
    "password": "Passw0rd!",
    "confirm": "Passw0rd!",
}


@allure.epic("Parabank UI")
@allure.feature("Регистрация")
class TestRegistration:

    @allure.story("Позитивный сценарий")
    @allure.title("Успешная регистрация нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.ui
    def test_registration_positive(self, driver, base_url):
        data = dict(VALID_DATA)
        data["username"] = unique_username("pos")

        page = RegistrationPage(driver, base_url)
        page.open_registration() \
            .fill_full_form(data) \
            .click_register()

        assert page.is_registration_successful(), "Регистрация не удалась"

    @allure.story("Негативный сценарий")
    @allure.title("Регистрация с пустым логином")
    @pytest.mark.negative
    @pytest.mark.ui
    def test_registration_empty_username(self, driver, base_url):
        data = dict(VALID_DATA)
        data["username"] = ""

        page = RegistrationPage(driver, base_url)
        page.open_registration() \
            .fill_full_form(data) \
            .click_register()

        assert "Username is required" in page.get_username_error()

    @allure.story("Негативный сценарий")
    @allure.title("Регистрация с пустым паролем")
    @pytest.mark.negative
    @pytest.mark.ui
    def test_registration_empty_password(self, driver, base_url):
        data = dict(VALID_DATA)
        data["username"] = unique_username("nopass")
        data["password"] = ""
        data["confirm"] = ""

        page = RegistrationPage(driver, base_url)
        page.open_registration() \
            .fill_full_form(data) \
            .click_register()

        assert "Password is required" in page.get_password_error()

    @allure.story("Негативный сценарий")
    @allure.title("Пароль и подтверждение не совпадают")
    @pytest.mark.negative
    @pytest.mark.ui
    def test_registration_password_mismatch(self, driver, base_url):
        data = dict(VALID_DATA)
        data["username"] = unique_username("mismatch")
        data["password"] = "Passw0rd!"
        data["confirm"] = "Different1!"

        page = RegistrationPage(driver, base_url)
        page.open_registration() \
            .fill_full_form(data) \
            .click_register()

        assert "Passwords did not match" in page.get_password_error()

    @allure.story("Негативный сценарий")
    @allure.title("Регистрация с пустым именем")
    @pytest.mark.negative
    @pytest.mark.ui
    def test_registration_empty_firstname(self, driver, base_url):
        data = dict(VALID_DATA)
        data["username"] = unique_username("nofn")
        data["first_name"] = ""

        page = RegistrationPage(driver, base_url)
        page.open_registration() \
            .fill_full_form(data) \
            .click_register()

        assert "First name is required" in page.get_firstname_error()

    @allure.story("Негативный сценарий")
    @allure.title("Регистрация с пустым SSN")
    @pytest.mark.negative
    @pytest.mark.ui
    def test_registration_empty_ssn(self, driver, base_url):
        data = dict(VALID_DATA)
        data["username"] = unique_username("nossn")
        data["ssn"] = ""

        page = RegistrationPage(driver, base_url)
        page.open_registration() \
            .fill_full_form(data) \
            .click_register()

        assert "Social Security Number is required" in page.get_ssn_error()
