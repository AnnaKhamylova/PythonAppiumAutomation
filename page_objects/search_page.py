from page_objects.base_page import (
    BasePageObject,
)

SEARCH_RESULT_LIST_ANDROID = "id:org.wikipedia:id/search_results_list"
SEARCH_RESULT_LIST_MWEB = 'xpath://*[@id="typeahead-suggestions"]/div'
SEARCH_BAR_MWEB = 'xpath://*[@id="minerva-overlay-search"]/div/div/div[1]'
SEARCH_RESULT_LIST_MWEB_AUTH = 'xpath://*[@id="v-1"]'
SEARCH_BAR_MWEB_IN_SEARCH = 'xpath://*[@id="minerva-overlay-search"]/div/div/div[1]/input'


class SearchPageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def search_result_list(self):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SEARCH_RESULT_LIST_ANDROID)
        elif self.platform == 'mobile_web':
            return self.wait_for_el_present(locator=SEARCH_RESULT_LIST_MWEB)

    def search_results_list_not_present(self):
        if self.platform == 'android':
            return self.wait_for_el_not_present(locator=SEARCH_RESULT_LIST_ANDROID)
        elif self.platform == 'mobile_web':
            return self.wait_for_el_not_present(locator=SEARCH_RESULT_LIST_MWEB)

    def article_in_list(self, locator_title):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=f"xpath://android.widget.TextView[@resource-id='org.wikipedia:id/page_list_item_title' and @text='{locator_title}']", error_message=f"Не нашли title статьи {locator_title}")
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=f"xpath:(//XCUIElementTypeStaticText[@name='{locator_title}'])[1]",
                                            error_message=f"Не нашли title статьи {locator_title}")
        elif self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=f"xpath:(//XCUIElementTypeStaticText[@name='{locator_title}'])[1]",
                                              error_message=f"Не нашли title статьи {locator_title}")

    def click_article_in_list(self, locator_title=None):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=f"xpath://android.widget.TextView[@resource-id='org.wikipedia:id/page_list_item_title' and @text='{locator_title}']", error_message=f"Не нашли title статьи {locator_title}")
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=f"xpath:(//XCUIElementTypeStaticText[@name='{locator_title}'])[1]",
                                              error_message=f"Не нашли title статьи {locator_title}")
        elif self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=f'xpath://*[@id="typeahead-suggestions"]/div/a[1]',
                                              error_message=f"Не нашли title статьи {locator_title}")

    def click_search_bar(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=SEARCH_BAR_MWEB)

    def send_keys_search(self, key):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_send_keys(locator=SEARCH_BAR_MWEB, keys=key)

    def search_result_list_auth(self):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SEARCH_RESULT_LIST_ANDROID)
        elif self.platform == 'mobile_web':
            return self.wait_for_el_present(locator=SEARCH_RESULT_LIST_MWEB_AUTH)

    def click_article_in_list_auth(self, locator_title=None):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=f'xpath://*[@id="v-2-33"]',
                                              error_message=f"Не нашли title статьи {locator_title}")

    def click_search_auth(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=SEARCH_BAR_MWEB_IN_SEARCH)

    def send_keys_search_auth(self, key):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_send_keys(locator=SEARCH_BAR_MWEB_IN_SEARCH, keys=key)

