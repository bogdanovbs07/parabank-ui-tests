import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from utils.attach import attach_screenshot, attach_browser_logs, attach_network_logs


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"])


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unknown browser: {browser}")

    driver.implicitly_wait(0)
    yield driver
  
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            attach_screenshot(driver)
            attach_browser_logs(driver)
            attach_network_logs(driver)
        except Exception as e:
            print(f"Ошибка при сборе артефактов: {e}")

    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return "https://parabank.parasoft.com/"


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
