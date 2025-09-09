
import pytest


class TestAndroid:
    def test_swipe_ios(self, set_up, main_page, portrait):
        main_page.click_skip_button()
        main_page.swipe_left(0.1)
        # main_page.assert_element_has_text(
        #     by="id",
        #     locator="org.wikipedia:id/primaryTextView",
        #     text="Новые способы исследований",
        # )
        # main_page.swipe_left(0.1)
        # main_page.assert_element_has_text(
        #     by="id",
        #     locator="org.wikipedia:id/primaryTextView",
        #     text="Списки для чтения с синхронизацией",
        # )
        # main_page.swipe_left(0.1)
        # main_page.assert_element_has_text(
        #     by="id",
        #     locator="org.wikipedia:id/primaryTextView",
        #     text="Отправлять отчёты об использовании",
        # )
        # main_page.click_accept_onboarding_button()
        # main_page.search_bar()