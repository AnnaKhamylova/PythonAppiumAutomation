import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver

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


@pytest.fixture(scope="function")
def driver_setup_teardown():
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
    print("setUp completed")
    yield driver
    driver.quit()
    print("teardown completed")


@pytest.fixture(scope="function")
def landscape(driver_setup_teardown):
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
def main_page(driver_setup_teardown):
    return MainPageObject(driver_setup_teardown)


@pytest.fixture(scope="function")
def search_page(driver_setup_teardown):
    return SearchPageObject(driver_setup_teardown)


@pytest.fixture(scope="function")
def article_page(driver_setup_teardown):
    return ArticlePageObject(driver_setup_teardown)


@pytest.fixture(scope="function")
def saved_articles_page(driver_setup_teardown):
    return SavedArticlesPageObject(driver_setup_teardown)
