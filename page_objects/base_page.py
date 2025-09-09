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
    def __init__(self, driver, set_up):
        self.driver = driver
        self.platform = set_up.platform

    # Раздел с методами
    def wait_for_el_present(
        self,
        locator,
        timeout=5,
        error_message="Элемент не найден",
    ):
        by = self.get_locator_by_string(locator)[0]
        locator_only = self.get_locator_by_string(locator)[1]
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (getattr(By, by.upper()), locator_only)
                )
            )
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_not_present(
        self,
        locator,
        timeout=5,
        error_message="Элемент не ушёл с экрана",
    ):
        by = self.get_locator_by_string(locator)[0]
        locator_only = self.get_locator_by_string(locator)[1]
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element(
                    (getattr(By, by.upper()), locator_only)
                )
            )
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_and_click(
        self,
        locator,
        timeout=10,
        error_message="Элемент не найден или не кликабелен",
    ):
        try:
            element = self.wait_for_el_present(
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
        locator,
        keys,
        timeout=5,
        error_message="Элемент не найден или не получилось отправить значения",
    ):
        try:
            element = self.wait_for_el_present(
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
        locator,
        attribute,
        timeout=5,
        error_message="Элемент не найден или не получилось получить атрибут",
    ):
        try:
            element = self.wait_for_el_present(
                locator=locator,
                timeout=timeout,
                error_message=error_message,
            )
            return element.get_attribute(attribute)
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def assert_element_has_text(
        self,
        locator,
        text,
        error_message="Текст в элементе и дочерних элементах не найден",
        timeout=5,
    ):
        try:
            element = self.wait_for_el_present(
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
        size = self.driver.get_window_size()
        y = size["height"] / 2
        start_x = size["width"] * 0.8
        end_x = size["width"] * 0.2
        if self.platform == 'android':
            actions = ActionChains(self.driver)
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

        elif self.platform == 'ios':
            self.driver.execute_script("mobile: dragFromToForDuration", {
                "fromX": start_x,
                "fromY": y,
                "toX": end_x,
                "toY": y,
                "duration": time_of_swipe
            })

    def assert_element_present(self, locator):
        by = self.get_locator_by_string(locator)[0]
        locator_only = self.get_locator_by_string(locator)[1]
        elements = self.driver.find_elements(
            getattr(By, by.upper()), locator_only
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

    def find_elements(self, locator):
        by = self.get_locator_by_string(locator)[0]
        locator_only = self.get_locator_by_string(locator)[1]
        return self.driver.find_elements(by, locator_only)

    @staticmethod
    def get_locator_by_string(locator_with_type: str):
        exploded_locator = locator_with_type.split(':', 1)
        by_type = exploded_locator[0]
        locator = exploded_locator[1]

        if by_type == 'xpath':
            return By.XPATH, locator
        elif by_type == 'id':
            return By.ID, locator
        elif by_type == 'name':
            return By.NAME, locator
        else:
            raise ValueError(f'Cannot get type of locator {locator_with_type}')
