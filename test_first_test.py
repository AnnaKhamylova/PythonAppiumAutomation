from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest


class TestFirst:
    @pytest.fixture(autouse=True)
    def __setup_class(self, driver_setup_teardown):
        self.driver = driver_setup_teardown

    def test_first(self):
        """Пример теста."""
        print(f'run first test')
        assert self.driver is not None, "Драйвер не инициализирован!"
