import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFirst:
    @pytest.fixture(autouse=True)
    def __setup_class(self, driver_setup_teardown):
        self.driver = driver_setup_teardown

    def wait_for_el_by_xpath(self, xpath, timeout=5, error_message='Элемент не найден'):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {xpath}'")

    def wait_for_el_and_click_by_xpath(self, xpath, timeout=5, error_message='Элемент не найден или не кликабелен'):
        try:
            element = self.wait_for_el_by_xpath(xpath=xpath, timeout=timeout, error_message=error_message)
            element.click()
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {xpath}'")

    def assert_element_has_text(self, locator, text,
                                error_message='Текст в элементе и дочерних элементах не найден', timeout=5):
        try:
            element = self.wait_for_el_by_xpath(xpath=locator, timeout=timeout)
            if element.text == text:
                return element
            else:
                children_with_text = element.find_elements(
                    By.XPATH, f'.//*[contains(@text, "{text}")]'
                )
                if len(children_with_text) > 0:
                    return children_with_text
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {element}'")

    def test_search_has_text(self):
        print(f'run first test')
        skip_button = self.wait_for_el_and_click_by_xpath(
            '//*[contains(@resource-id, "org.wikipedia:id/fragment_onboarding_skip_button")]'
        )
        search_bar = self.wait_for_el_by_xpath('//*[contains(@resource-id, "org.wikipedia:id/search_container")]')
        search_bar_with_text = self.assert_element_has_text(
            '//*[contains(@resource-id, "org.wikipedia:id/search_container")]', 'Поиск по Википедии')