import json
import allure


def attach_screenshot(driver):
    png = driver.get_screenshot_as_png()
    allure.attach(png, name="screenshot", attachment_type=allure.attachment_type.PNG)


def attach_browser_logs(driver):
    try:
        logs = driver.get_log("browser")
        allure.attach(
            json.dumps(logs, indent=2, ensure_ascii=False),
            name="browser_logs",
            attachment_type=allure.attachment_type.JSON,
        )
    except Exception as e:
        allure.attach(str(e), name="browser_logs_error", attachment_type=allure.attachment_type.TEXT)


def attach_network_logs(driver):
    try:
        logs = driver.get_log("performance")
        allure.attach(
            json.dumps(logs, indent=2, ensure_ascii=False),
            name="network_logs",
            attachment_type=allure.attachment_type.JSON,
        )
    except Exception as e:
        allure.attach(str(e), name="network_logs_error", attachment_type=allure.attachment_type.TEXT)
