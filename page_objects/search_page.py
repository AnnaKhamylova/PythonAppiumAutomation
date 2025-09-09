from page_objects.base_page import (
    BasePageObject,
)


class SearchPageObject(BasePageObject):

    def search_result_list(self):
        return self.wait_for_el_present(
            by="id", locator="org.wikipedia:id/search_results_list"
        )

    def search_results_list_not_present(self):
        return self.wait_for_el_not_present(
            by="id", locator="org.wikipedia:id/search_results_list"
        )

    def article_in_list(self, locator_title):
        return self.wait_for_el_present(
            by="xpath",
            locator=locator_title,
            error_message=f"Не нашли title статьи {locator_title}",
        )

    def click_article_in_list(self, locator_title):
        return self.wait_for_el_and_click(
            by="xpath",
            locator=locator_title,
            error_message=f"Не нашли title статьи {locator_title}",
        )
