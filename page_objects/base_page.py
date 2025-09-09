import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import (
    ActionBuilder,
)
from selenium.webdriver.common.actions.pointer_input import (
    PointerInput,
)
from selenium.webdriver.common.actions import interaction


class BasePageObject:
    def __init__(self, driver):
        self.driver = driver

    # Раздел с методами
    def wait_for_el_present(
        self,
        by,
        locator,
        timeout=5,
        error_message="Элемент не найден",
    ):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (getattr(By, by.upper()), locator)
                )
            )
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_not_present(
        self,
        by,
        locator,
        timeout=5,
        error_message="Элемент не ушёл с экрана",
    ):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element(
                    (getattr(By, by.upper()), locator)
                )
            )
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_and_click(
        self,
        by,
        locator,
        timeout=10,
        error_message="Элемент не найден или не кликабелен",
    ):
        try:
            element = self.wait_for_el_present(
                by=by,
                locator=locator,
                timeout=timeout,
                error_message=error_message,
            )
            element.click()
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_and_send_keys(
        self,
        by,
        locator,
        keys,
        timeout=5,
        error_message="Элемент не найден или не получилось отправить значения",
    ):
        try:
            element = self.wait_for_el_present(
                by=by,
                locator=locator,
                timeout=timeout,
                error_message=error_message,
            )
            element.send_keys(keys)
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_and_get_attribute(
        self,
        by,
        locator,
        attribute,
        timeout=5,
        error_message="Элемент не найден или не получилось получить атрибут",
    ):
        try:
            element = self.wait_for_el_present(
                by=by,
                locator=locator,
                timeout=timeout,
                error_message=error_message,
            )
            return element.get_attribute(attribute)
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def assert_element_has_text(
        self,
        by,
        locator,
        text,
        error_message="Текст в элементе и дочерних элементах не найден",
        timeout=5,
    ):
        try:
            element = self.wait_for_el_present(
                by=by,
                locator=locator,
                timeout=timeout,
                error_message=error_message,
            )
            if element.text == text:
                return element
            else:
                children_with_text = element.find_elements(
                    By.XPATH, f'.//*[contains(@text, "{text}")]'
                )
                if len(children_with_text) > 0:
                    return children_with_text
                pytest.fail(
                    f"{error_message} | Ожидаемый текст: '{text}' | Фактический текст: '{element.text}' | Локатор: {locator}"
                )
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def swipe_left(self, time_of_swipe):
        actions = ActionChains(self.driver)
        size = self.driver.get_window_size()
        y = size["height"] / 2
        start_x = size["width"] * 0.8
        end_x = size["width"] * 0.2
        actions.w3c_actions = ActionBuilder(
            self.driver,
            mouse=PointerInput(interaction.POINTER_TOUCH, "finger"),
        )
        (
            actions.w3c_actions.pointer_action.move_to_location(
                start_x, y
            )
            .pointer_down()
            .move_to_location(end_x, y)
            .pause(time_of_swipe)
            .pointer_up()
        )
        actions.perform()

    def assert_element_present(self, by, locator):
        elements = self.driver.find_elements(
            getattr(By, by.upper()), locator
        )
        assert len(elements) > 0, "Нашли 0 элементов!"

    def click_on_the_screen(self):
        size = self.driver.get_window_size()
        center_x = size["width"] // 2
        center_y = size["height"] // 2
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(
            center_x, center_y
        )
        actions.w3c_actions.pointer_action.click()
        actions.perform()

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)
