import time

from selenium.webdriver.common.by import By


class TestFirst:

    def test_first(self, main_page):
        """Пример теста."""
        print("run first test")
        assert (
            main_page.driver is not None
        ), "Драйвер не инициализирован!"

    def test_search_has_text(self, main_page, portrait):
        """Проверяет наличие текста в поисковой строке"""
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.assert_element_has_text(
            by="xpath",
            locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]',
            text="Поиск по Википедии",
        )

    def test_cancel_search(self, main_page, portrait):
        """Проверяет наличие текста в поисковой строке"""
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.assert_element_has_text(
            by="xpath",
            locator='//*[contains(@resource-id, "org.wikipedia:id/search_container")]',
            text="Поиск по Википедии",
        )
        main_page.send_keys_search(keys="Appium")
        main_page.search_close()
        main_page.search_close_not_present()

    def test_cancel_search_for_ex(
        self, main_page, search_page, portrait
    ):
        """Что делает тест:
        - Ищет какое-то слово
        - Убеждается, что найдено несколько статей
        - Отменяет поиск
        - Убеждается, что результат поиска пропал"""
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys="Appium")
        search_page.search_result_list()
        article_list = search_page.find_elements(
            By.ID, "org.wikipedia:id/page_list_item_title"
        )
        assert article_list, "Список статей пуст!"
        main_page.search_close()
        main_page.search_close_not_present()
        search_page.search_results_list_not_present()

    def test_find_words_in_search_result_for_ex(
        self, main_page, search_page, portrait
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        search_result = search_page.search_result_list()
        article_list = search_result.find_elements(
            By.ID, "org.wikipedia:id/page_list_item_title"
        )
        assert article_list, "Список статей пуст!"
        for article in article_list:
            article_text = article.text
            assert (
                key_word in article_text
            ), f"Текст '{key_word}' не найден в элементе {article}. Текст элемента: '{article_text}'"

    def test_swipe(self, main_page, portrait):
        main_page.assert_element_has_text(
            by="id",
            locator="org.wikipedia:id/secondaryTextView",
            text="Мы нашли следующие языки на вашем устройстве:",
        )
        main_page.swipe_left(0.1)
        main_page.assert_element_has_text(
            by="id",
            locator="org.wikipedia:id/primaryTextView",
            text="Новые способы исследований",
        )
        main_page.swipe_left(0.1)
        main_page.assert_element_has_text(
            by="id",
            locator="org.wikipedia:id/primaryTextView",
            text="Списки для чтения с синхронизацией",
        )
        main_page.swipe_left(0.1)
        main_page.assert_element_has_text(
            by="id",
            locator="org.wikipedia:id/primaryTextView",
            text="Отправлять отчёты об использовании",
        )
        main_page.click_accept_onboarding_button()
        main_page.search_bar()

    def test_article_has_title(
        self,
        main_page,
        search_page,
        article_page,
        saved_articles_page,
        portrait,
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        main_page.search_result()
        locator_title = "//*[@resource-id='org.wikipedia:id/page_list_item_title'and @text='Python']"
        search_page.click_article_in_list(locator_title=locator_title)
        article_page.wait_for_el_and_click(
            by="xpath",
            locator="//*[@resource-id='org.wikipedia:id/page_save' and @text='Сохранить']",
        )
        article_page.wait_for_el_and_click(
            by="xpath",
            locator="//*[@resource-id='org.wikipedia:id/snackbar_action' and @text='Добавить в список']",
        )
        article_page.wait_for_el_and_send_keys(
            by="xpath",
            locator="//*[@resource-id='org.wikipedia:id/text_input' and @text='Название этого списка']",
            keys="Python",
        )
        article_page.wait_for_el_and_click(
            by="xpath",
            locator="//*[@resource-id='android:id/button1' and @text='ОК']",
        )
        article_page.wait_for_el_and_click(
            by="xpath",
            locator="//*[@resource-id='org.wikipedia:id/snackbar_action' and @text='Посмотреть список']",
        )
        saved_articles_page.wait_for_el_and_click(
            by="xpath",
            locator="//*[@resource-id='org.wikipedia:id/page_list_item_title' and @text='Python']",
        )
        saved_articles_page.assert_element_present(
            by="xpath",
            locator='//android.view.View[@resource-id="pcs"]/android.view.View[1]//*[contains(@text, "Python")]',
        )

    def test_change_screen_orientation(
        self, portrait, main_page, search_page, article_page
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        search_page.search_result_list()
        locator_title = "//*[@resource-id='org.wikipedia:id/page_list_item_title'and @text='Python']"
        search_page.article_in_list(locator_title=locator_title)
        search_page.click_article_in_list(locator_title=locator_title)
        time.sleep(3)
        search_page.click_on_the_screen()
        article_title_before_rotation = article_page.wait_for_el_and_get_attribute(
            by="xpath",
            locator='//android.view.View[@resource-id="pcs"]/android.view.View[1]',
            attribute="text",
        )
        article_page.driver.orientation = "LANDSCAPE"
        article_title_after_rotation = article_page.wait_for_el_and_get_attribute(
            by="xpath",
            locator='//android.view.View[@resource-id="pcs"]/android.view.View[1]',
            attribute="text",
        )
        assert (
            article_title_before_rotation == article_title_after_rotation
        ), "Заголовок статьи до и после ротации экрана не равны!"

    def test_check_search_article_in_background(
        self, main_page, search_page, article_page, portrait
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        search_page.search_result_list()
        locator_title = "//*[@resource-id='org.wikipedia:id/page_list_item_title'and @text='Python']"
        search_page.article_in_list(locator_title=locator_title)
        search_page.driver.background_app(2)
        search_page.article_in_list(locator_title=locator_title)
