import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

class TestFirst:
    @pytest.fixture(autouse=True)
    def __setup_class(self, driver_setup_teardown):
        self.driver = driver_setup_teardown

    def wait_for_el_present(self, by, locator, timeout=5, error_message='Элемент не найден'):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(
                (getattr(By, by.upper()), locator))
            )
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_not_present(self, by, locator, timeout=5, error_message='Элемент не ушёл с экрана'):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(
                (getattr(By, by.upper()), locator))
            )
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_and_click(self, by, locator, timeout=5,
                              error_message='Элемент не найден или не кликабелен'):
        try:
            element = self.wait_for_el_present(by=by, locator=locator, timeout=timeout, error_message=error_message)
            element.click()
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def wait_for_el_and_send_keys(self, by, locator, keys, timeout=5,
                                  error_message='Элемент не найден или не получилось отправить значения'):
        try:
            element = self.wait_for_el_present(by=by, locator=locator, timeout=timeout, error_message=error_message)
            element.send_keys(keys)
            return element
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def assert_element_has_text(self, by, locator, text,
                                error_message='Текст в элементе и дочерних элементах не найден', timeout=5):
        try:
            element = self.wait_for_el_present(by=by, locator=locator, timeout=timeout, error_message=error_message)
            if element.text == text:
                return element
            else:
                children_with_text = element.find_elements(
                    By.XPATH, f'.//*[contains(@text, "{text}")]'
                )
                if len(children_with_text) > 0:
                    return children_with_text
        except Exception:
            pytest.fail(f"{error_message} | Локатор: {locator}'")

    def swipe_left(self, time_of_swipe):
        actions = ActionChains(self.driver)
        size = self.driver.get_window_size()
        y = size['height'] / 2
        start_x = size['width'] * 0.8
        end_x = size['width'] * 0.2
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "finger"))
        (actions.w3c_actions
         .pointer_action
         .move_to_location(start_x, y)
         .pointer_down()
         .move_to_location(end_x, y)
         .pause(time_of_swipe)
         .pointer_up())
        actions.perform()

    def test_first(self):
        """Пример теста."""
        print(f'run first test')
        assert self.driver is not None, "Драйвер не инициализирован!"

    def test_search_has_text(self):
        """Проверяет наличие текста в поисковой строке"""
        skip_button = self.wait_for_el_and_click(by='xpath',
                                                 locator='//*[contains(@resource-id, "org.wikipedia:id/fragment_onboarding_skip_button")]')
        search_bar = self.wait_for_el_present(by='xpath',
                                              locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]')
        search_bar_with_text = self.assert_element_has_text(by='xpath',
                                                            locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]',
                                                            text='Поиск по Википедии')

    def test_cancel_search(self):
        """Проверяет наличие текста в поисковой строке"""
        skip_button = self.wait_for_el_and_click(by='xpath',
                                                 locator='//*[contains(@resource-id, '
                                                         '"org.wikipedia:id/fragment_onboarding_skip_button")]')
        search_bar = self.wait_for_el_present(by='xpath',
                     locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]')
        search_bar_with_text = self.assert_element_has_text(
            by='xpath', locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]',
            text='Поиск по Википедии')
        search_bar.click()
        search_edit_frame = self.wait_for_el_and_send_keys(by='xpath',
                                                           locator='//android.widget.AutoCompleteTextView'
                                                                   '[@resource-id="org.wikipedia:id/search_src_text"]',
                                                           keys='Appium')
        search_close = self.wait_for_el_and_click(by='id', locator='org.wikipedia:id/search_close_btn')
        self.wait_for_el_not_present(by='id', locator='org.wikipedia:id/search_close_btn')

    def test_cancel_search_for_ex(self):
        """Что делает тест:
            - Ищет какое-то слово
            - Убеждается, что найдено несколько статей
            - Отменяет поиск
            - Убеждается, что результат поиска пропал"""
        skip_button = self.wait_for_el_and_click(by='xpath',
                                                 locator='//*[contains(@resource-id, '
                                                         '"org.wikipedia:id/fragment_onboarding_skip_button")]')
        search_bar = self.wait_for_el_and_click(by='xpath',
                                              locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]')
        search_edit_frame = self.wait_for_el_and_send_keys(by='xpath',
                                                           locator='//android.widget.AutoCompleteTextView'
                                                                   '[@resource-id="org.wikipedia:id/search_src_text"]',
                                                           keys='Appium')
        search_result = self.wait_for_el_present(by='id', locator='org.wikipedia:id/search_results_list')
        article_list = search_result.find_elements(By.ID, "org.wikipedia:id/page_list_item_title")
        assert article_list, "Список статей пуст!"
        search_close = self.wait_for_el_and_click(by='id', locator='org.wikipedia:id/search_close_btn')
        self.wait_for_el_not_present(by='id', locator='org.wikipedia:id/search_close_btn')
        self.wait_for_el_not_present(by='id', locator='org.wikipedia:id/search_results_list')

    def test_find_words_in_search_result_for_ex(self):
        key_word = 'Python'
        skip_button = self.wait_for_el_and_click(by='xpath',
                                                 locator='//*[contains(@resource-id, '
                                                         '"org.wikipedia:id/fragment_onboarding_skip_button")]')
        search_bar = self.wait_for_el_and_click(by='xpath',
                                                locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]')
        search_edit_frame = self.wait_for_el_and_send_keys(by='xpath',
                                                           locator='//android.widget.AutoCompleteTextView'
                                                                   '[@resource-id="org.wikipedia:id/search_src_text"]',
                                                           keys=key_word)
        search_result = self.wait_for_el_present(by='id', locator='org.wikipedia:id/search_results_list')
        article_list = search_result.find_elements(By.ID, "org.wikipedia:id/page_list_item_title")
        assert article_list, "Список статей пуст!"
        for article in article_list:
            article_text = article.text
            assert key_word in article_text, f"Текст '{key_word}' не найден в элементе {article}. Текст элемента: '{article_text}'"

    def test_swipe(self):
        first_screen = self.assert_element_has_text(by='id', locator='org.wikipedia:id/secondaryTextView',
                                                    text='Мы нашли следующие языки на вашем устройстве:')
        self.swipe_left(0.1)
        second_screen = self.assert_element_has_text(by='id', locator='org.wikipedia:id/primaryTextView',
                                                     text='Новые способы исследований')
        self.swipe_left(0.1)
        third_screen = self.assert_element_has_text(by='id', locator='org.wikipedia:id/primaryTextView',
                                                    text='Списки для чтения с синхронизацией')
        self.swipe_left(0.1)
        fourth_screen = self.assert_element_has_text(by='id', locator='org.wikipedia:id/primaryTextView',
                                                    text='Отправлять отчёты об использовании')
        accept_button = self.wait_for_el_and_click(by='id', locator='org.wikipedia:id/acceptButton')
        search_bar = self.wait_for_el_present(by='xpath',
                                                locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]')
