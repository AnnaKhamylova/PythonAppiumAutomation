from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest


@pytest.mark.usefixtures("driver_setup_teardown")
class TestFirst:

    @pytest.fixture()
    def driver_setup_teardown(self):
        options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "Android",
            "appium:deviceName": "emulator-5554",
            "appium:platformVersion": "15.0",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "org.wikipedia",
            "appium:appActivity": ".main.MainActivity",
            "appium:app": "/Users/akhamylova/PycharmProjects/PythonAppiumAutomation/org.wikipedia.apk"
        }
            )
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        print('setUp completed')
        yield
        self.driver.quit()
        print('teardown completed')

    def test_first(self):
        """Пример теста."""
        print(f'run first test')
        assert self.driver is not None, "Драйвер не инициализирован!"
