import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver


@pytest.fixture(scope="function")
def driver_setup_teardown():
    options = UiAutomator2Options().load_capabilities(
    {
         "platformName": "Android",
         "appium:deviceName": "emulator-5554",
         "appium:automationName": "UiAutomator2",
         "appium:appPackage": "org.wikipedia",
         "appium:appActivity": ".main.MainActivity",
         "appium:app": "/Users/akhamylova/PycharmProjects/PythonAppiumAutomation/org.wikipedia.apk"
    }
        )
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    print('setUp completed')
    yield driver
    driver.quit()
    print('teardown completed')
