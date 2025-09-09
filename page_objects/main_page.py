from page_objects.base_page import (
    BasePageObject,
)


class MainPageObject(BasePageObject):
    pass

    def click_skip_button(self):
        return self.wait_for_el_and_click(
            by="xpath",
            locator="//*[contains(@resource-id, "
            '"org.wikipedia:id/fragment_onboarding_skip_button")]',
        )

    def click_search_bar(self):
        return self.wait_for_el_and_click(
            by="xpath",
            locator="//*[contains(@resource-id, "
            '"org.wikipedia:id/search_container")]',
        )

    def search_bar(self):
        return self.wait_for_el_present(
            by="xpath",
            locator="//*[contains(@resource-id, "
            '"org.wikipedia:id/search_container")]',
        )

    def send_keys_search(self, keys):
        return self.wait_for_el_and_send_keys(
            by="xpath",
            locator="//android.widget.AutoCompleteTextView"
            '[@resource-id="org.wikipedia:id/search_src_text"]',
            keys=keys,
        )

    def search_close(self):
        return self.wait_for_el_and_click(
            by="id", locator="org.wikipedia:id/search_close_btn"
        )

    def search_close_not_present(self):
        return self.wait_for_el_not_present(
            by="id", locator="org.wikipedia:id/search_close_btn"
        )

    def search_result(self):
        return self.wait_for_el_present(
            by="id", locator="org.wikipedia:id/search_results_list"
        )

    def click_accept_onboarding_button(self):
        return self.wait_for_el_and_click(
            by="id", locator="org.wikipedia:id/acceptButton"
        )
