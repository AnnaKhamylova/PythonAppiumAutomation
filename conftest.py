import os

import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.options.ios import XCUITestOptions

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


@pytest.fixture()
def driver_setup_teardown(set_up):
    options = None
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
    else:
        raise ValueError('Передайте существующую платформу: ios или android')
    driver = webdriver.Remote(
        "http://127.0.0.1:4723", options=options
        )
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
