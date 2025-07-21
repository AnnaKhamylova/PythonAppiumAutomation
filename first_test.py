from appium import webdriver
from appium.options.android import UiAutomator2Options


class FirstTest:
    def __init__(self):
        options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "Android",
            "appium:deviceName": "emulator-5554",
            "appium:platformVersion": "15.0",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "org.wikipedia",
            "appium:appActivity": ".main.MainActivity",
            "appium:app": "/Users/akhamylova/PycharmProjects/pythonProject1/org.wikipedia.apk"
        }
        )
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        print('first test run')

    def __del__(self):
        self.driver.quit()


first_test_init = FirstTest()
