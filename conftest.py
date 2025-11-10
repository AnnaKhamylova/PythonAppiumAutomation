import os
import time

import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By

from page_objects.article_page import (
    ArticlePageObject,
)
from page_objects.main_page import (
    MainPageObject,
)
from page_objects.saved_articles_page import (
    SavedArticlesPageObject,
)
from page_objects.search_page import (
    SearchPageObject,
)
from page_objects.welcome_page import WelcomePageObject


class SetUp:
    def __init__(self, platform):
        self.platform = platform


@pytest.fixture
def driver_setup_teardown(set_up):
    driver = None
    if set_up.platform == 'android':
        options = UiAutomator2Options().load_capabilities(
            {
                "platformName": "Android",
                "appium:deviceName": "emulator-5554",
                "appium:automationName": "UiAutomator2",
                "appium:appPackage": "org.wikipedia",
                "appium:appActivity": ".main.MainActivity",
                "appium:app": "/Users/akhamylova/PycharmProjects/PythonAppiumAutomation/org.wikipedia.apk",
            }
        )
        driver = webdriver.Remote(
            "http://127.0.0.1:4723", options=options
        )
    elif set_up.platform == 'ios':
        options = XCUITestOptions().load_capabilities(
            {
                "platformName": "iOS",
                "appium:deviceName": "iPhone 16 Pro Max",
                "appium:platformVersion": "18.5",
                "appium:appPackage": "org.wikipedia",
                "appium:appActivity": ".main.MainActivity",
                "appium:automationName": "XCUITest",
                "appium:app": "/Users/akhamylova/PycharmProjects/PythonAppiumAutomation/Wikipedia.app"
            }
        )
        driver = webdriver.Remote(
            "http://127.0.0.1:4723", options=options
        )
    elif set_up.platform == 'mobile_web':
        from selenium import webdriver as selenium_webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver.chrome.service import Service
        import subprocess

        try:
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
        except:
            chromedriver_path = '/Users/akhamylova/webdrivers/chromedriver'
            try:
                subprocess.run(['xattr', '-d', 'com.apple.quarantine', chromedriver_path],
                               check=True, capture_output=True)
            except subprocess.CalledProcessError:
                pass

            service = Service(executable_path=chromedriver_path)

        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        }
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = selenium_webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.wikipedia.org/")

    print("setUp completed")
    yield driver
    driver.quit()
    print("teardown completed")


@pytest.fixture(scope="function")
def landscape(driver_setup_teardown=None):
    original_orientation = "LANDSCAPE"
    driver_setup_teardown.orientation = original_orientation
    yield
    driver_setup_teardown.orientation = original_orientation


@pytest.fixture(scope="function")
def portrait(driver_setup_teardown):
    original_orientation = "PORTRAIT"
    driver_setup_teardown.orientation = original_orientation
    yield
    driver_setup_teardown.orientation = original_orientation


@pytest.fixture(scope="function")
def main_page(driver_setup_teardown, set_up):
    return MainPageObject(driver_setup_teardown, set_up)


@pytest.fixture(scope="function")
def search_page(driver_setup_teardown, set_up):
    return SearchPageObject(driver_setup_teardown, set_up)


@pytest.fixture(scope="function")
def article_page(driver_setup_teardown, set_up):
    return ArticlePageObject(driver_setup_teardown, set_up)


@pytest.fixture(scope="function")
def saved_articles_page(driver_setup_teardown, set_up):
    return SavedArticlesPageObject(driver_setup_teardown, set_up)


@pytest.fixture(scope="function")
def welcome_page(driver_setup_teardown, set_up):
    return WelcomePageObject(driver_setup_teardown, set_up)


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default=os.environ.get("PLATFORM", "android"),
        help="Platform to run tests: android or ios"
    )


@pytest.fixture(scope="function")
def set_up(request):
    platform = request.config.getoption("--platform").lower()
    return SetUp(platform=platform)


@pytest.fixture
def auto_cleanup_saved_articles(driver_setup_teardown, set_up, saved_articles_page):
    driver = driver_setup_teardown
    yield driver
    if set_up.platform == 'mobile_web':
        unwatch_buttons = driver.find_elements(By.XPATH, '//a[contains(@href, "action=unwatch")]')
        for button in unwatch_buttons:
            button.click()
            time.sleep(2)
            saved_articles_page.refresh_page()
            unwatch_buttons = driver.find_elements(By.XPATH, '//a[contains(@href, "action=unwatch")]')
        print(f"Удалено сохранений: {len(unwatch_buttons)}")

