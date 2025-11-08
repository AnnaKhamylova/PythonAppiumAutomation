class TestIos:
    def test_swipe_ios(self, set_up, main_page, portrait, welcome_page):
        welcome_page.first_page()
        welcome_page.swipe_left(0.1)
        welcome_page.second_page()
        welcome_page.swipe_left(0.1)
        welcome_page.third_page()
        welcome_page.swipe_left(0.1)
        welcome_page.fourth_page()
        welcome_page.click_reject_button()
        main_page.search_bar()
