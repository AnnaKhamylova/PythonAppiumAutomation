import time
import allure


@allure.epic("Проверки мвеба")
class TestsMWeb:

    @allure.feature("Проверки драйвера")
    @allure.title("Проверяем запуск драйвера")
    @allure.description("Тестовый тест")
    def test_first(self, set_up, main_page):
        """Пример теста."""
        print("run first test")
        assert (
            main_page.driver is not None
        ), "Драйвер не инициализирован!"

    @allure.feature("Проверки сохраненных статей")
    @allure.title("Удаляем статью Python из сохраненных")
    @allure.description("Добавляем несколько статей в сохранённые и удаляем оттуда статью с title=Python")
    def test_delete_article_from_saved(self, set_up, welcome_page, main_page, search_page, article_page,
                                       saved_articles_page, auto_cleanup_saved_articles):
        driver = auto_cleanup_saved_articles
        with allure.step("Step 1. Ищем по слову Python"):
            key_word = 'Python'
            main_page.click_search_bar()
            main_page.send_keys_search(keys=key_word)
            search_page.search_result_list()
        with allure.step("Step 2. Кликаем на первый результат в списке"):
            search_page.click_article_in_list()
        with allure.step("Step 3. Логинимся"):
            main_page.open_menu()
            time.sleep(1)
            main_page.open_login()
            main_page.login()
            main_page.click_login()
            time.sleep(5)
        with allure.step("Step 4. Сохраняем статью Python"):
            article_page.click_save_button()
            time.sleep(2)
        with allure.step("Step 5. Открываем рандомную статью"):
            main_page.open_menu()
            time.sleep(1)
            main_page.open_random()
            time.sleep(2)
        with allure.step("Step 6. Сохраняем рандомную статью"):
            article_page.click_save_button()
            time.sleep(1)
        with allure.step("Step 7. Открываем список сохранённых статей"):
            main_page.open_menu_auth_after_random()
            time.sleep(1)
            main_page.open_watchlist()
            time.sleep(2)
        with allure.step("Step 8. Убираем статью Python из сохранённых статей"):
            saved_articles_page.undo_saving(title='Python')
            time.sleep(1)
        with allure.step("Step 9. Обновляем страницу и смотрим, что в списке нет статьи Python"):
            saved_articles_page.refresh_page()
            time.sleep(1)
            saved_articles_page.check_saved_article_not_title(title='Python')