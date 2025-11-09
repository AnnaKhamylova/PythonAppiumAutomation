import time


class TestsAndroid:
    def test_first(self, set_up, main_page):
        """Пример теста."""
        print("run first test")
        assert (
            main_page.driver is not None
        ), "Драйвер не инициализирован!"

    def test_search_has_text(self, set_up, welcome_page, main_page, portrait):
        """Проверяет наличие текста в поисковой строке"""
        welcome_page.click_skip_button()
        main_page.click_search_bar()
        if set_up.platform == 'android':
            main_page.assert_element_has_text(
                locator='xpath://*[contains(@resource-id, "org.wikipedia:id/search_container")]',
                text="Поиск по Википедии"
            )

    def test_cancel_search(self, set_up, main_page, portrait):
        """Проверяет наличие текста в поисковой строке"""
        main_page.click_skip_button()
        main_page.click_search_bar()
        if set_up.platform == 'android':
            main_page.assert_element_has_text(
                locator='xpath://*[contains(@resource-id, "org.wikipedia:id/search_container")]',
                text="Поиск по Википедии"
            )
        main_page.send_keys_search(keys="Appium")
        main_page.search_close()
        main_page.search_close_not_present()

    def test_cancel_search_for_ex(
        self, set_up, main_page, search_page, portrait
    ):
        """Что делает тест:
        - Ищет какое-то слово
        - Убеждается, что найдено несколько статей
        - Отменяет поиск
        - Убеждается, что результат поиска пропал"""
        if set_up.platform == 'android':

            main_page.click_skip_button()
            main_page.click_search_bar()
            main_page.send_keys_search(keys="Appium")
            search_page.search_result_list()
            article_list = search_page.find_elements(locator="id:org.wikipedia:id/page_list_item_title")
            assert article_list, "Список статей пуст!"
            main_page.search_close()
            main_page.search_close_not_present()
            search_page.search_results_list_not_present()

    def test_find_words_in_search_result_for_ex(
        self, set_up, main_page, search_page, portrait
    ):
        if set_up.platform == 'android':
            key_word = "Python"
            main_page.click_skip_button()
            main_page.click_search_bar()
            main_page.send_keys_search(keys=key_word)
            search_page.search_result_list()
            article_list = search_page.find_elements(locator="id:org.wikipedia:id/page_list_item_title")
            assert article_list, "Список статей пуст!"
            for article in article_list:
                article_text = article.text
                assert (
                    key_word in article_text
                ), f"Текст '{key_word}' не найден в элементе {article}. Текст элемента: '{article_text}'"

    def test_swipe(self, set_up, welcome_page, main_page, portrait):
        welcome_page.first_page()
        welcome_page.swipe_left(0.1)
        welcome_page.second_page()
        welcome_page.swipe_left(0.1)
        welcome_page.third_page()
        welcome_page.swipe_left(0.1)
        welcome_page.fourth_page()
        welcome_page.click_reject_button()
        main_page.search_bar()

    def test_article_has_title(
        self,
        set_up,
        main_page,
        search_page,
        article_page,
        saved_articles_page,
        portrait
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        main_page.search_result()
        search_page.click_article_in_list(locator_title=key_word)
        if set_up.platform == 'ios':
            article_page.article_name(article_name=key_word)
        else:
            article_page.click_save_button()
            article_page.click_add_to_list()
            article_page.send_keys_list_name(keys=key_word)
            article_page.click_create_list_ok()
            article_page.click_see_list(name=key_word)
            saved_articles_page.click_article(name=key_word)
            saved_articles_page.assert_element_present(locator='xpath://android.view.View[@resource-id="pcs"]/android.view.View[1]//*[contains(@text, "Python")]')

    def test_change_screen_orientation(
        self, set_up, main_page, search_page, article_page
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        search_page.search_result_list()
        locator_title = "Python"
        search_page.article_in_list(locator_title=locator_title)
        search_page.click_article_in_list(locator_title=locator_title)
        time.sleep(3)
        search_page.click_on_the_screen()
        article_title_before_rotation = article_page.article_name(article_name=key_word)
        article_page.driver.orientation = "LANDSCAPE"
        article_title_after_rotation = article_page.article_name(article_name=key_word)
        assert (
            article_title_before_rotation == article_title_after_rotation
        ), "Заголовок статьи до и после ротации экрана не равны!"

    def test_check_search_article_in_background(
        self, set_up, main_page, search_page, article_page, portrait
    ):
        key_word = "Python"
        main_page.click_skip_button()
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        search_page.search_result_list()
        locator_title = "Python"
        search_page.article_in_list(locator_title=locator_title)
        search_page.driver.background_app(2)
        search_page.article_in_list(locator_title=locator_title)
