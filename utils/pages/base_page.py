import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str = None):
        self.driver.get(url or self.url)
        return self

    @allure.step("Найти элемент по локатору: {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти видимый элемент по локатору: {locator}")
    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    @allure.step("Ввести '{text}' в поле: {locator}")
    def type(self, locator, text: str):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
