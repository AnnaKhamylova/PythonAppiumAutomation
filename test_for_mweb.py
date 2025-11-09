import time


class TestsMWeb:
    def test_first(self, set_up, main_page):
        """Пример теста."""
        print("run first test")
        assert (
            main_page.driver is not None
        ), "Драйвер не инициализирован!"

    def test_delete_article_from_two_saved(self, set_up, welcome_page, main_page, search_page, article_page,
                                           saved_articles_page, auto_cleanup_saved_articles):
        """Удаляем одну сохраненную статью из двух"""
        driver = auto_cleanup_saved_articles
        key_word = 'Python'
        main_page.click_search_bar()
        main_page.send_keys_search(keys=key_word)
        search_page.search_result_list()
        search_page.click_article_in_list()
        main_page.open_menu()
        time.sleep(1)
        main_page.open_login()
        main_page.login()
        main_page.click_login()
        time.sleep(5)
        article_page.click_save_button()
        time.sleep(2)
        main_page.open_menu()
        main_page.open_menu_auth()
        time.sleep(2)
        article_page.click_save_button()
        main_page.open_menu_auth_after_random()
        main_page.open_watchlist()
        time.sleep(2)
        saved_articles_page.check_list_len(2)
        saved_articles_page.undo_saving(title='Python')
        saved_articles_page.refresh_page()
        saved_articles_page.check_list_len(1)
        saved_articles_page.check_saved_article_not_title(title='Python')