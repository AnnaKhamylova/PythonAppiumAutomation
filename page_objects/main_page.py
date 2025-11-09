import time

from page_objects.base_page import (
    BasePageObject,
)

SEARCH_BAR_ANDROID = 'xpath://*[contains(@resource-id, "org.wikipedia:id/search_container")]'
SEARCH_BAR_MWEB = 'xpath://*[@id="searchInput"]'
SEARCH_FIELD_IOS = 'name:Поиск по Википедии'
SEARCH_CONTAINER_ANDROID = 'id:org.wikipedia:id/search_src_text'
SEARCH_CLOSE_BUTTON_ANDROID = "id:org.wikipedia:id/search_close_btn"
SEARCH_BACK = 'xpath://android.widget.ImageButton[@content-desc="Перейти вверх"]'
SEARCH_CLOSE_BUTTON_IOS = 'name:Очистить текст'
SEARCH_RESULT_LIST = "id:org.wikipedia:id/search_results_list"
SKIP_BUTTON_IOS = 'name:Пропустить'
SKIP_BUTTON_ANDROID = 'xpath://*[contains(@resource-id, "org.wikipedia:id/fragment_onboarding_skip_button")]'

class MainPageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def click_skip_button(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SKIP_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=SKIP_BUTTON_IOS)

    def click_search_bar(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SEARCH_BAR_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=SEARCH_FIELD_IOS)
        elif self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=SEARCH_BAR_MWEB)

    def search_bar(self):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SEARCH_BAR_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=SEARCH_FIELD_IOS)

    def send_keys_search(self, keys):
        if self.platform == 'android':
            return self.wait_for_el_and_send_keys(locator=SEARCH_CONTAINER_ANDROID, keys=keys)
        elif self.platform == 'ios':
            return self.wait_for_el_and_send_keys(locator=SEARCH_FIELD_IOS, keys=keys)
        elif self.platform == 'mobile_web':
            return self.wait_for_el_and_send_keys(locator=SEARCH_BAR_MWEB, keys=keys)

    def search_close(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SEARCH_CLOSE_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=SEARCH_CLOSE_BUTTON_IOS)

    def search_back(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SEARCH_BACK)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=SEARCH_CLOSE_BUTTON_IOS)

    def search_close_not_present(self):
        if self.platform == 'android':
            return self.wait_for_el_not_present(locator=SEARCH_CLOSE_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_not_present(locator=SEARCH_CLOSE_BUTTON_IOS)

    def search_result(self):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SEARCH_RESULT_LIST)

    def login(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_send_keys(locator='xpath://*[@id="wpName1"]', keys='Admranev2025'), self.wait_for_el_and_send_keys(locator='xpath://*[@id="wpPassword1"]', keys='parol20203')

    def open_menu(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator='xpath://*[@id="mw-mf-page-center"]/header/div/nav[1]')

    def open_login(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator='xpath://*[@id="p-personal"]')

    def click_login(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator='xpath://*[@id="userloginForm"]/form/div[6]/div')

    def open_menu_auth(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator='xpath://*[@id="p-navigation"]/li[2]')

    def open_menu_auth_after_random(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator='xpath://*[@id="mw-mf-page-center"]/header/div/nav[1]')

    def open_watchlist(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator = 'xpath://*[@id="p-personal"]/li[3]')

