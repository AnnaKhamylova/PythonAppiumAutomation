from page_objects.base_page import (
    BasePageObject,
)

SEARCH_RESULT_LIST_ANDROID = "id:org.wikipedia:id/search_results_list"


class SearchPageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def search_result_list(self):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SEARCH_RESULT_LIST_ANDROID)

    def search_results_list_not_present(self):
        if self.platform == 'android':
            return self.wait_for_el_not_present(locator=SEARCH_RESULT_LIST_ANDROID)

    def article_in_list(self, locator_title):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=f"xpath://android.widget.TextView[@resource-id='org.wikipedia:id/page_list_item_title' and @text='{locator_title}']", error_message=f"Не нашли title статьи {locator_title}")
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=f"xpath:(//XCUIElementTypeStaticText[@name='{locator_title}'])[1]",
                                            error_message=f"Не нашли title статьи {locator_title}")

    def click_article_in_list(self, locator_title):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=f"xpath://android.widget.TextView[@resource-id='org.wikipedia:id/page_list_item_title' and @text='{locator_title}']", error_message=f"Не нашли title статьи {locator_title}")
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=f"xpath:(//XCUIElementTypeStaticText[@name='{locator_title}'])[1]",
                                              error_message=f"Не нашли title статьи {locator_title}")

